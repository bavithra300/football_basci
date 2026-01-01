def generate_report(players, position):
    report = f"\n⚽ COACH REPORT – TOP {position.upper()}S\n\n"

    for p in players:
        report += f"""
Player: {p['name']}
Age: {p['age']}
Position: {position}
Wins / Losses: {p['wins']} / {p['losses']}
Fitness: {p['fitness']}
Coach Score: {p['coach_score']}

Coach Insight:
Reliable performer with tactical discipline and match impact.
---------------------------------------
"""
    return report
