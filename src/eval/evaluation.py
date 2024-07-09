import jsonlines
import json
import os
from tqdm import tqdm
from .math_normalization import *
import tiktoken
encoding = tiktoken.get_encoding('cl100k_base')


def answer_cleansing(pred_str):
    pattern = 'The answer is (.*)$'
    preds = re.findall(pattern, pred_str)
    pred = preds[-1] if len(preds) > 0 else ''

    pred = pred.replace(",", "")
    pred = [s for s in re.findall(r'-?\d+\.?\d*', pred)]

    # If there is no candidate in list, null is set.
    if len(pred) == 0:
        pred = ""
    else:
        pred = pred[0]

    # (For arithmetic tasks) if a word ends with period, it will be omitted ...
    if pred != "":
        if pred[-1] == ".":
            pred = pred[:-1]

    return pred


def test_answer(pred_str, ans_str, answer_key):
    pattern = "{} (.*)$".format(answer_key)
    if "Question" in pred_str:
        pred_str = pred_str.split("Question")[0]
    pred_str = pred_str.strip()
    preds = re.findall(pattern, pred_str)
    pred = preds[-1] if len(preds) > 0 else ''

    if pred == '':
        pred = answer_cleansing(pred_str)

    if "</s>" in pred:
        pred = pred[:-4]
    gold = ans_str

    pred = normalize_final_answer(pred)
    gold = normalize_final_answer(gold)
    return check_sympy_equivalence(gold, pred), pred, gold


def parser_pred_ans(preds_str, golds_str, properties_list, answer_key):
    results, preds, golds = [], [], []
    for pred_str, gold_str, properties in tqdm(zip(preds_str, golds_str, properties_list), total=len(preds_str)):
        result, pred, gold = test_answer(pred_str, gold_str, answer_key)
        results.append(result)
        preds.append(pred)
        golds.append(gold)
    return results, preds, golds


def get_results(pred_file, dev_set, answer_key):
    acc = 0
    gold_data = [json.loads(line) for line in open(f'data/test/{dev_set}.jsonl')]
    pred_data = [json.loads(line) for line in open(pred_file)]

    new_data = []
    for gold_instance, pred_instance in zip(gold_data, pred_data):
        gold_str = gold_instance['answer']
        pred_str = pred_instance['response']
        result, pred, gold = test_answer(pred_str, gold_str, answer_key)

        pred_instance['pred'] = pred
        pred_instance['gold'] = gold
        pred_instance['result'] = result
        new_data.append(pred_instance)

        acc += int(result)

    assert len(new_data) == len(pred_data)
    with open(os.path.join(os.path.dirname(pred_file), 'results.jsonl'), 'w') as f:
        for instance in new_data:
            f.write(json.dumps(instance) + '\n')
    print('Results saved to %s' % os.path.join(os.path.dirname(pred_file), 'results.jsonl'))

    print('acc:', acc / len(new_data))
    metrics = {'acc': acc / len(new_data)}
    with open(os.path.join(os.path.dirname(pred_file), 'metrics.json'), 'w') as f:
        json.dump(metrics, f)
