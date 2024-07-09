import json
import random
import re

direct_prompt = "Question: {}\nAnswer:"


def convert_gsm8k_to_test(input_filename, output_filename, tag='GSM8K_TRAIN_2'):
    data = [json.loads(line) for line in open(input_filename)]
    new_data = []
    for instance in data:
        pattern = "#### (.*)$"
        preds = re.findall(pattern, instance['answer'])
        assert len(preds) == 1
        pred = preds[-1]

        if instance['answer'][-len(pred):] != pred:
            pass

        new_instance = {
            'source': tag,
            'question': instance['question'],
            'solution': instance['answer'],
            'answer': pred,
            'tag': {}
        }
        new_data.append(new_instance)

    assert len(new_data) == len(data)
    print(len(new_data))
    print(new_data[0])
    with open(output_filename, 'w') as f:
        for instance in new_data:
            f.write(json.dumps(instance) + '\n')
    print('Saved to', output_filename)


def convert_math_to_test(input_filename, output_filename, tag='MATH_TRAIN_2'):
    data = [json.loads(line) for line in open(input_filename)]
    new_data = []
    for instance in data:
        new_instance = {
            'source': tag,
            'question': instance['problem'],
            'solution': instance['solution'],
            'answer': instance['answer'],
            'tag': {'subject': instance['subject'], 'level': instance['level'], 'unique_id': instance['unique_id']}
        }
        new_data.append(new_instance)

    assert len(new_data) == len(data)
    print(len(new_data))
    print(new_data[0])
    with open(output_filename, 'w') as f:
        for instance in new_data:
            f.write(json.dumps(instance) + '\n')
    print('Saved to', output_filename)


def convert_gsm8k_to_llamafactory(input_filename, output_filename):
    data = [json.loads(line) for line in open(input_filename)]
    new_data = []

    for id, instance in enumerate(data):
        prompt = direct_prompt.format(instance['question'])
        answer = re.sub(r'<<.*?>>', '', instance['answer'])
        new_instance = {
            "id": id,
            "content": prompt,
            "output": answer
        }
        new_data.append(new_instance)

    print(len(new_data))
    print(new_data[0])
    with open(output_filename, 'w') as f:
        json.dump(new_data, f, indent=4)
    print('Saved to', output_filename)


def convert_math_to_llamafactory(input_filename, output_filename):
    data = [json.loads(line) for line in open(input_filename)]
    new_data = []

    for id, instance in enumerate(data):
        new_instance = {
            "id": id,
            "content": direct_prompt.format(instance['problem']),
            "output": instance['solution'] + ' The answer is: ' + instance['answer']
        }
        new_data.append(new_instance)

    print(len(new_data))
    print(new_data[0])
    with open(output_filename, 'w') as f:
        json.dump(new_data, f, indent=4)
    print('Saved to', output_filename)


if __name__ == '__main__':
    convert_gsm8k_to_test('raw/gsm8k/train_2.jsonl', 'test/gsm8k_train_2.jsonl', tag='GSM8K_TRAIN_2')
    convert_math_to_test('raw/math/train_2.jsonl', 'test/math_train_2.jsonl', tag='MATH_TRAIN_2')

    convert_gsm8k_to_llamafactory('raw/gsm8k/train_2.jsonl', 'llama_factory/gsm8k/gsm8k_train_2.json')
    convert_math_to_llamafactory('raw/math/train_2.jsonl', 'llama_factory/math/math_train_2.json')
