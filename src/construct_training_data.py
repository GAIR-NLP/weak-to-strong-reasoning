import os
import json
import copy
import random
from collections import Counter

direct_prompt = "Question: {}\nAnswer:"


def construct_full_weak_data(input_filename, output_filename):
    data = [json.loads(line) for line in open(input_filename)]  # generated by weak model

    new_data = []
    acc = 0
    for instance in data:
        id = instance['id']
        response = instance['response']
        if instance['result']:
            acc += 1

        new_instance = {
            'id': id,
            'content': instance['prompt'],
            'output': response
        }
        new_data.append(new_instance)

    print(acc / len(new_data))
    print(len(new_data))
    print(new_data[0])
    with open(output_filename, 'w') as f:
        json.dump(new_data, f, indent=4)
    print(f'Saved to {output_filename}')


def construct_weak_icl_data(weak_filename, icl_filename, output_filename):
    weak_data = [json.loads(line) for line in open(weak_filename)]  # generated by M_weak
    icl_data = [json.loads(line) for line in open(icl_filename)]  # generated by M_icl
    assert len(weak_data) == len(icl_data)

    new_data = []
    new_data_weak = []
    new_data_icl = []
    acc = 0
    for weak_instance, icl_instance in zip(weak_data, icl_data):
        assert weak_instance['id'] == icl_instance['id']

        if weak_instance['pred'] != '' and weak_instance['pred'] == icl_instance['pred']:
            if weak_instance['result']:
                acc += 1

            new_instance = {
                'id': weak_instance['id'],
                'content': weak_instance['prompt'],
                'output': weak_instance['response']
            }
            new_data.append(new_instance)
            new_data_weak.append(new_instance)

            new_icl_instance = copy.deepcopy(new_instance)
            new_icl_instance['output'] = icl_instance['response']
            new_data.append(new_icl_instance)
            new_data_icl.append(new_icl_instance)

    print(acc / len(weak_data))

    print(len(new_data))
    print(new_data[0])
    with open(output_filename, 'w') as f:
        json.dump(new_data, f, indent=4)
    print(f'Saved to {output_filename}')

    print(len(new_data_weak))
    output_filename1 = output_filename.replace('_hybrid.json', '_weak.json')
    with open(output_filename1, 'w') as f:
        json.dump(new_data_weak, f, indent=4)
    print(f'Saved to {output_filename1}')

    print(len(new_data_icl))
    output_filename2 = output_filename.replace('_hybrid.json', '_icl.json')
    with open(output_filename2, 'w') as f:
        json.dump(new_data_icl, f, indent=4)
    print(f'Saved to {output_filename2}')


def construct_majority_voting_data(data_dir, seed_start=0, seed_end=10):
    data = []
    for seed in range(seed_start, seed_end):
        filename = os.path.join(data_dir, f'seed{seed}/results.jsonl')
        data.append([json.loads(line) for line in open(filename)])

    new_data = []
    for instances in zip(*data):
        new_instance = {
            'id': instances[0]['id'],
            'prompt': instances[0]['prompt'],
            'gold': instances[0]['gold'],
            'pos_responses': [],
            'neg_responses': [],
            'confidence': 0
        }

        preds = [ins['pred'] for ins in instances]
        counts = Counter(preds)
        most_common_pred, most_common_num = counts.most_common(1)[0]
        new_instance['confidence'] = most_common_num / len(instances)
        for ins in instances:
            if ins['pred'] == most_common_pred:
                new_instance['pos_responses'].append({'response': ins['response'], 'pred': ins['pred'], 'result': ins['result']})
            else:
                new_instance['neg_responses'].append({'response': ins['response'], 'pred': ins['pred'], 'result': ins['result']})
        new_data.append(new_instance)

    print(len(new_data))
    print(new_data[0])
    output_filename = os.path.join(data_dir, 'majority_voting_results.jsonl')
    with open(output_filename, 'w') as f:
        for ins in new_data:
            f.write(json.dumps(ins) + '\n')
    print('Saved to', output_filename)


def construct_paired_data_gsm8k(weak_filename, weak_llamafactory_filename, majority_voting_filename, output_filename, confidence=0.8):
    weak_data = [json.loads(line) for line in open(weak_filename)]  # results.jsonl
    weak_llamafactory_data = json.load(open(weak_llamafactory_filename))  # *_full_weak.json
    majority_voting_data = [json.loads(line) for line in open(majority_voting_filename)]
    assert len(weak_data) == len(weak_llamafactory_data) == len(majority_voting_data)

    random.seed(42)
    new_data = []
    weak_pos = 0
    weak_neg = 0
    acc = 0
    for weak_instance, weak_llamafactory_instance, majority_voting_instance in zip(weak_data, weak_llamafactory_data, majority_voting_data):
        assert weak_instance['id'] == weak_llamafactory_instance['id'] == majority_voting_instance['id']
        assert weak_instance['response'] == weak_llamafactory_instance['output']
        if majority_voting_instance['confidence'] < 0.6:
            continue
        if majority_voting_instance['pos_responses'][0]['pred'] == '':
            continue

        if weak_instance['pred'] == majority_voting_instance['pos_responses'][0]['pred']:
            # weak_instance作为正样例
            if len(majority_voting_instance['neg_responses']) == 0:
                # 太简单
                continue

            negative_response = random.sample(majority_voting_instance['neg_responses'], 1)[0]['response']
            new_instance = {
                'id': weak_instance['id'],
                'instruction': weak_llamafactory_instance['content'],
                'input': '',
                'output': [weak_llamafactory_instance['output'], negative_response]
            }
            new_data.append(new_instance)
            weak_pos += 1

            if weak_instance['result']:
                acc += 1
        elif majority_voting_instance['confidence'] >= confidence:
            # weak_instance作为负样例
            assert weak_instance['pred'] != majority_voting_instance['pos_responses'][0]['pred']
            positive_response = random.sample(majority_voting_instance['pos_responses'], 1)[0]['response']
            new_instance = {
                'id': weak_instance['id'],
                'instruction': weak_llamafactory_instance['content'],
                'input': '',
                'output': [positive_response, weak_llamafactory_instance['output']]
            }
            new_data.append(new_instance)
            weak_neg += 1

            if majority_voting_instance['pos_responses'][0]['result']:
                acc += 1

    print(len(new_data))
    print(new_data[0])
    print(weak_pos, weak_neg)
    print(acc / len(new_data))
    with open(output_filename, 'w') as f:
        json.dump(new_data, f, indent=4)
    print(f'Saved to {output_filename}')


def construct_paired_data_math(weak_filename, weak_llamafactory_filename, majority_voting_filename, output_filename, confidence=0.8):
    weak_data = [json.loads(line) for line in open(weak_filename)]  # results.jsonl
    weak_llamafactory_data = json.load(open(weak_llamafactory_filename))  # *_full_weak.json
    majority_voting_data = [json.loads(line) for line in open(majority_voting_filename)]
    assert len(weak_data) == len(weak_llamafactory_data) == len(majority_voting_data)

    random.seed(42)
    new_data = []
    weak_pos = 0
    weak_neg = 0
    acc = 0
    for weak_instance, weak_llamafactory_instance, majority_voting_instance in zip(weak_data, weak_llamafactory_data, majority_voting_data):
        assert weak_instance['id'] == weak_llamafactory_instance['id'] == majority_voting_instance['id']
        assert weak_instance['response'] == weak_llamafactory_instance['output']
        if majority_voting_instance['confidence'] < 0.6:
            continue
        if majority_voting_instance['pos_responses'][0]['pred'] == '':
            continue

        if weak_instance['pred'] == majority_voting_instance['pos_responses'][0]['pred']:
            # weak_instance作为正样例
            if len(majority_voting_instance['neg_responses']) == 0:
                # 太简单
                continue

            if len(majority_voting_instance['neg_responses']) > 3:
                negative_instances = random.sample(majority_voting_instance['neg_responses'], 3)
            else:
                negative_instances = majority_voting_instance['neg_responses']
            for negative_instance in negative_instances:
                negative_response = negative_instance['response']
                new_instance = {
                    'id': weak_instance['id'],
                    'instruction': weak_llamafactory_instance['content'],
                    'input': '',
                    'output': [weak_llamafactory_instance['output'], negative_response]
                }
                new_data.append(new_instance)
                weak_pos += 1

                if weak_instance['result']:
                    acc += 1
        elif majority_voting_instance['confidence'] >= confidence:
            # weak_instance作为负样例
            assert weak_instance['pred'] != majority_voting_instance['pos_responses'][0]['pred']
            positive_response = random.sample(majority_voting_instance['pos_responses'], 1)[0]['response']
            new_instance = {
                'id': weak_instance['id'],
                'instruction': weak_llamafactory_instance['content'],
                'input': '',
                'output': [positive_response, weak_llamafactory_instance['output']]
            }
            new_data.append(new_instance)
            weak_neg += 1

            if majority_voting_instance['pos_responses'][0]['result']:
                acc += 1

            positive_num = 1
            for positive_instance in majority_voting_instance['pos_responses']:
                if positive_instance['response'] != positive_response:
                    new_instance = {
                        'id': weak_instance['id'],
                        'instruction': weak_llamafactory_instance['content'],
                        'input': '',
                        'output': [positive_instance['response'], weak_llamafactory_instance['output']]
                    }
                    new_data.append(new_instance)
                    weak_neg += 1

                    if positive_instance['result']:
                        acc += 1

                    positive_num += 1
                    if positive_num >= 3:
                        break

    print(len(new_data))
    print(new_data[0])
    print(weak_pos, weak_neg)
    print(acc / len(new_data))
    with open(output_filename, 'w') as f:
        json.dump(new_data, f, indent=4)
    print(f'Saved to {output_filename}')


if __name__ == '__main__':
    pass
