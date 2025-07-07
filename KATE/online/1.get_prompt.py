import json
import random
from openai import OpenAI
import re
from codebleu import calc_codebleu


def cal_codebleu(prediction, reference):
    result = calc_codebleu(
        [reference],
        [prediction],
        lang="java",
        weights=(0.25, 0.25, 0.25, 0.25),
        tokenizer=None,
    )
    return result["codebleu"] * 100


def sava_jsonl(path, data):
    with open(path, "w", encoding="utf-8") as jsonl_file:
        for item in data:
            json.dump(item, jsonl_file, ensure_ascii=False)
            jsonl_file.write("\n")


def read_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as jsonl_file:
        for line in jsonl_file:
            item = json.loads(line.strip())
            data.append(item)
    return data


data = read_jsonl("your_test_data")
for item in data:
    Message_X = item["best_commit_message"]
    dependency = item["dependency"]
    field = item["field"]
    public_information = dependency + " " + field
    edit_seq = item["edit_seq"]
    ast_seq = item["ast_edit_seq_with_pruning"]
    Changes_X = f"public_information:{public_information},line-level diff sequence:{edit_seq},ast-level diff sequence:{ast_seq}"
    refer_test_src = item["refer_test_src"]
    refer_test_tgt = item["refer_test_tgt"]
    Template_X = f"refer_test_src:{refer_test_src},refer_test_tgt:{refer_test_tgt}"
    T = item["test_src"]
    prompt = f"Please update the test code {T} when the production code is changed, based on the given production code changes {Changes_X} and the commit message {Message_X}. We find a similar code-to-test co-evolution case in our repositories as a reference, with {Template_X} in that case. Return the updated code only without any comment."
    item["prompt"] = prompt
sava_jsonl("your_output_path", data)
