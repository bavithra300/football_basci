def rank_players(players, top_n=5):
    return sorted(players, key=lambda x: x["coach_score"], reverse=True)[:top_n]
