def polish_answer(answer: str):
    answer = answer.strip()

    answer = answer.split(")")[0]
    answer = answer.strip()

    if "(" in answer:
        try:
            answer = answer.split("(")[1]
            answer = answer.strip()
        except:
            pass

    answer = answer.split(" ")[0]

    if len(answer)>0:
        return answer[0]
    return answer