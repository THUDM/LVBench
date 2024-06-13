from lvbench.metrics.compute_accuracy import compute_accuracy

def main():
    result = compute_accuracy("random_answers.json", "../data/video_info.meta.jsonl")
    print(result)
if __name__ == '__main__':
    main()