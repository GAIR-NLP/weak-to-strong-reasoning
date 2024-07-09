import os
import json
import argparse
import warnings
warnings.filterwarnings("ignore")

from .model import Models
from .prompt import get_prompts
from .eval import get_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_dir', type=str, default="./")
    parser.add_argument('--output_file_name', type=str, default='output.json')
    parser.add_argument('--template', type=str)
    parser.add_argument('--dev_set', type=str, default='all')
    parser.add_argument('--prompt_type', type=str, default='few-shot')
    parser.add_argument('--answer_key', type=str, default='####')
    parser.add_argument('--instruction_type', type=str, default='normal')
    parser.add_argument('--model_type', type=str, default='vllm')
    parser.add_argument('--trust_remote_code', type=bool, default=True)
    parser.add_argument('--max_tokens', type=int, default=1024)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--temperature', type=float, default=0.0)
    parser.add_argument('--top_p', type=float, default=1.0)
    parser.add_argument('--presence_penalty', type=float, default=0.0)
    parser.add_argument('--frequency_penalty', type=float, default=0.0)
    parser.add_argument('--logprobs', type=int, default=None)
    parser.add_argument('--prompt_logprobs', type=int, default=None)
    parser.add_argument('--stop', type=str, nargs='+', default=['Question', '#'], help="you can pass one or multiple stop strings to halt the generation process.")
    parser.add_argument('--max_num_batched_tokens', type=int, default=32768)
    parser.add_argument('--eval_only', action='store_true')
    args = parser.parse_args()
    print(args)

    if not args.eval_only:
        model = Models[args.model_type](args)
        processed_prompts = get_prompts(args.dev_set, args.template, args.prompt_type, args.answer_key,
                                        args.instruction_type)
        outputs = model.generate(processed_prompts)
        print(outputs[0].outputs[0].text)

        if not os.path.exists(os.path.dirname(args.output_file_name)):
            os.makedirs(os.path.dirname(args.output_file_name), exist_ok=True)
        with open(args.output_file_name, 'w') as f:
            for id, output in enumerate(outputs):
                prompt = output.prompt
                response = output.outputs[0].text.strip().strip(".")
                f.write(json.dumps({'id': id, 'prompt': prompt, 'response': response}) + '\n')
        print("Saved to {}".format(args.output_file_name))
        
    get_results(args.output_file_name, args.dev_set, args.answer_key)
