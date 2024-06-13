import os
import json

def main():
    input_file = "../data/video_info.meta.jsonl"
    output_file = "videos.txt"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(input_file,"r") as f:
        lines = [line.strip() for line in f.readlines()]

        for line in lines:
            try:
                data = json.loads(line)
                video_url = f"https://www.youtube.com/watch?v={data['key']}"
            except:
                continue
            with open(output_file,"a") as f:
                f.write(video_url + "\n")

if __name__ == '__main__':
    main()