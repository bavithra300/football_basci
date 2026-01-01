def analyze(players):
    analyzed = []

    for p in players:
        score = (p["fitness"] * 0.5) + (p["wins"] * 0.3) - (p["losses"] * 0.2)
        p["coach_score"] = round(score, 2)
        analyzed.append(p)

    return analyzed
