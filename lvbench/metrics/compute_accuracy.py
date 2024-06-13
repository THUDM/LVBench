import json
import jsonlines
from collections import defaultdict

def compute_accuracy(answer_file: str, video_meta_file: str):
    total_qa_num = 0
    right_num = 0
    category_right = defaultdict(int)
    category_total = defaultdict(int)
    category_acc = defaultdict(int)

    with open(answer_file) as f:
        model_answers = json.load(f)

    with jsonlines.open(video_meta_file) as reader:
        video_meta = list(reader)
        for meta_data in video_meta:
            for qa in meta_data['qa']:
                uid = str(qa["uid"])
                if uid in model_answers:
                    model_answer = model_answers[uid]
                    for category in qa['question_type']:
                        category_total[category] += 1
                        if model_answer == qa["answer"]:
                            category_right[category] += 1
                    if model_answer == qa["answer"]:
                        right_num += 1
                    total_qa_num += 1

    for key in category_total:
        category_acc[key] = category_right[key] / category_total[key]

    acc = float(right_num) / total_qa_num
    category_acc.update({"acc": acc})
    return category_acc

if __name__ == '__main__':
    compute_accuracy("results/gemini_answers.json", "data/test.jsonl")
