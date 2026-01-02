def generate_report(ranked_players):
    report = "🔥 TOP PLAYER RECOMMENDATIONS 🔥\n\n"
    for i, p in enumerate(ranked_players, 1):
        report += f"{i}. {p['name']} ({p['club']}) - Score: {p['score']}\n"
    return report
