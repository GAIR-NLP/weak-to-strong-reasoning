import os
import json
import argparse
from datasets import load_dataset, concatenate_datasets
import transformers
import torch
import gc
import warnings
warnings.filterwarnings("ignore")
from .model import Models
from .prompt import templates


def load_data(hf_data_path, split):
    """
    It is ok to test only a subset (e.g., only English subset),
    You can filter the desired data by modifying this function.
    """

    subjects = ["Math", "Physics", "Chemistry", "Biology", "Geography", "Astronomy"]
    datasets = []
    for subject in subjects:
        dataset = load_dataset(hf_data_path, subject, split=split)
        # only English
        dataset = dataset.filter(lambda x: x['language'] == 'EN')
        dataset = dataset.filter(lambda x: x['answer_type'] != 'CODE' and x['answer_type'] != 'OT')
        datasets.append(dataset)
        print(subject, len(dataset))
    datasets = concatenate_datasets(datasets)
    print(len(datasets))
    return datasets


def get_prompts(dataset, args):
    data = []
    prompt_list = []
    for instance in dataset:
        vllm_prompt = instance['prompt'].replace('\n\nproblem:\n', '\n\nQuestion: ') + '\n\nAnswer:'
        if args.prompt_type == 'few-shot':
            demonstrations = templates[args.template]
            vllm_prompt = demonstrations + vllm_prompt

        instance['vllm_prompt'] = vllm_prompt
        prompt_list.append(vllm_prompt)
        data.append(instance)

    assert len(data) == len(prompt_list)
    print(len(data))
    print(data[0])
    output_filename = os.path.join(os.path.dirname(args.output_filename), 'input.jsonl')
    with open(output_filename, 'w') as f:
        for instance in data:
            f.write(json.dumps(instance) + '\n')
    print("Saved to {}".format(output_filename))

    return data, prompt_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--hf_data_path', type=str, default="GAIR/OlympicArena")
    parser.add_argument("--split", type=str, default="val")
    parser.add_argument('--template', type=str, default='zero_shot')
    parser.add_argument('--prompt_type', type=str, default='zero-shot')

    parser.add_argument('--model_type', type=str, default='vllm')
    parser.add_argument("--model", type=str, default="llama3-8b-instruct")
    parser.add_argument("--model_dir", type=str, default='./')
    parser.add_argument('--output_filename', type=str, default='output.jsonl')

    parser.add_argument('--trust_remote_code', type=bool, default=True)
    parser.add_argument('--max_tokens', type=int, default=2048)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--temperature', type=float, default=0.0)
    parser.add_argument('--top_p', type=float, default=1.0)
    parser.add_argument('--presence_penalty', type=float, default=0.0)
    parser.add_argument('--frequency_penalty', type=float, default=0.0)
    parser.add_argument('--logprobs', type=int, default=None)
    parser.add_argument('--prompt_logprobs', type=int, default=None)
    parser.add_argument('--stop', type=str, nargs='+', default=[], help="you can pass one or multiple stop strings to halt the generation process.")
    parser.add_argument('--max_num_batched_tokens', type=int, default=32768)

    args = parser.parse_args()
    pipeline = transformers.pipeline(
        "text-generation",
        model=args.model_dir,
        device_map="auto",
    )
    args.stop += [pipeline.tokenizer.eos_token, "<|eot_id|>"]
    if not os.path.exists(os.path.dirname(args.output_filename)):
        os.makedirs(os.path.dirname(args.output_filename), exist_ok=True)
    print(args)

    dataset = load_data(args.hf_data_path, args.split)
    data, processed_prompts = get_prompts(dataset, args)
    print(processed_prompts[0])
    del pipeline
    gc.collect()
    torch.cuda.empty_cache()

    model = Models[args.model_type](args)
    outputs = model.generate(processed_prompts)
    print(outputs[0].outputs[0].text)

    with open(args.output_filename, 'w') as f:
        for instance, output in zip(data, outputs):
            assert instance['vllm_prompt'] == output.prompt
            instance['response'] = output.outputs[0].text
            f.write(json.dumps(instance) + '\n')
    print("Saved to {}".format(args.output_filename))
