def winner(names: list[str] ,scores:list[float]) -> str:
    best_score=scores[0]
    best_name=names[0]
    for name, score in zip(names,scores):
        if score > best_score:
            best_score = score
            best_name= name
    return best_name
