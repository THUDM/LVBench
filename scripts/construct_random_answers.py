import random
import jsonlines
import json
def main():
    video_meta_file = "../data/video_info.meta.jsonl"
    output_file = "random_answers.json"
    with jsonlines.open(video_meta_file) as reader:
        video_meta = list(reader)

    results = {}
    for meta_data in video_meta:
        for qa in meta_data['qa']:
            uid = qa["uid"]
            results[uid] = random.choice(['A','B','C','D'])

    with open(output_file, 'w') as f:
        json.dump(results, f)


if __name__ == '__main__':
    main()