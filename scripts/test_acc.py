import json

from lvbench.metrics.compute_accuracy import compute_accuracy


def main():
    result = compute_accuracy("random_answers.json", "../data/video_info.meta.jsonl")
    print(result)

    # generate result.json for leaderboard: https://huggingface.co/spaces/THUDM/LVBench
    name_map = {"key information retrieval": "KIR", "event understanding": "EU", "summarization": "Sum",
                "entity recognition": "ER", "reasoning": "Rea", "temporal grounding": "TG", "acc": "Overall"}
    with open("result.json",'w') as f:
        json.dump({name_map[k]:v for k,v in result.items()}, f, indent=4)
        print(f"result.json generated! You can submit your results to https://huggingface.co/spaces/THUDM/LVBench")




if __name__ == '__main__':
    main()
