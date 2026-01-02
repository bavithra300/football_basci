def analyze(players):
    for p in players:
        p["score"] = p["rating"] * 1.1
    return players
