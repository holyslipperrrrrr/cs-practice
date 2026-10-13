
def winner(names ,scores) -> str:
    best_score=scores[0]
    best_name=names[0]
    for name, score in zip(names,scores):
        if score > best_score:
            best_score = score
            best_name= name
    return best_name


def average(scores) -> float:
    if len(scores)==0:
        return 0.0
    else:
        return round(sum(scores)/len(scores),2)



def ranking(names: list[str],scores: list[float]) -> list[str]:
    pairs = sorted(zip(names, scores), key=lambda pair: pair[1], reverse=True)
    return [name for name, score in pairs]


def above_average(names: list[str],scores: list [float]) -> list[str]:
    sr=average(scores)
    result=[]
    for name,score in zip(names,scores):
        if score> sr:
            result.append(name)
    return result





if __name__=="__main__":
    names =  ["Аня", "Боря", "Вика"]
    scores = [7.0,   9.0,    9.0]
    print(winner(names,scores))
