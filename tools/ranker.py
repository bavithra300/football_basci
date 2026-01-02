def rank(players):
    return sorted(players, key=lambda x: x["score"], reverse=True)
