from agent.coach_agent import coach_agent
from agent.planner import plan_tools
from tools.web_search import search_players
from tools.extractor import extract_player_stats
from report.coach_report import generate_report

position = input("Enter position (Goalkeeper / Defender / Midfielder / Forward): ")

print("\n🧠 Agent Reasoning:\n")
print(coach_agent(position))

plan = plan_tools(position)
raw_data = search_players(plan["search_query"])

players_text = extract_player_stats(raw_data, position)

print("\n📋 FINAL COACH REPORT\n")
print(players_text)
