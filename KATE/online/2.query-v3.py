import json
import random
from openai import OpenAI
import re


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


def extract_java_block(text):
    pattern = r"```java(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return text.strip()


data = read_jsonl("input_jsonl_path")

openai = OpenAI(
    api_key="your_api_key",
    base_url="your_base_url",
)

model = "your_model"
prompt_key = "prompt"
content_key = "content"
for idx, item in enumerate(data):
    if content_key in item.keys():
        continue
    prompt = item[prompt_key]
    try:
        chat_completion = openai.chat.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}], stream=False
        )
        print(f"{idx}: success")
    except Exception as e:
        print(f"{idx}: {str(e)}")
        continue
    content = chat_completion.choices[0].message.content
    item[content_key] = extract_java_block(content)
sava_jsonl("output_jsonl_path", data)
