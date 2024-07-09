import jsonlines

from .templates import templates

InstructionList = {
    "direct": "Question: [INPUT]\nAnswer:",
    # "llama3": "<|begin_of_text|>[DEMO]Question: [INPUT]\nAnswer:",
}


def get_prompts(dev_set, template_source, prompt_type, answer_key, instruction_type):
    data = []
    with open(r"data/test/{}.jsonl".format(dev_set)) as f:
        for line in jsonlines.Reader(f):
            data.append(line)
            data = [line for line in data]
    prompt_list = []
    for line in data:
        if prompt_type == 'few-shot':
            prompt = templates[template_source]
        else:
            prompt = templates["math-single"]
        processed_prompt = prompt.replace("[ANSWERKEY]", answer_key)
        if '[DEMO]' in InstructionList[instruction_type]:
            processed_prompt = InstructionList[instruction_type].replace("[DEMO]", processed_prompt)
        else:
            processed_prompt = processed_prompt + InstructionList[instruction_type]
        processed_prompt = processed_prompt.replace("[INPUT]", line['question'])
        prompt_list.append(processed_prompt)

    print('num:', len(prompt_list))
    print(prompt_list[0])

    return prompt_list
