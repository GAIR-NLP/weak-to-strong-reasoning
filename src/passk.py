import os
import json


def passk(data_dir, seed_start=0, seed_end=10):
    data = []
    for seed in range(seed_start, seed_end):
        filename = os.path.join(data_dir, f'seed{seed}/results.jsonl')
        data.append([json.loads(line) for line in open(filename)])

    acc = 0
    for instances in zip(*data):
        # 只要有一个正确的，就算这个sample正确
        if any([ins['result'] for ins in instances]):
            acc += 1

    print(f'data_dir: {data_dir}')
    print(f'len(data): {len(data[0])}')
    print(f'passk: {acc / len(data[0])}')


if __name__ == '__main__':
    pass
