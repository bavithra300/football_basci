from agent.coach_agent import coach_agent
from agent.planner import planner

from tools.web_search import web_search
from tools.extractor import extract
from tools.analyzer import analyze
from tools.ranker import rank

from report.coach_report import generate_report

def run(position):
    coach_output = coach_agent(position)
    plan = planner(coach_output)

    raw_data = web_search(position)
    extracted = extract(raw_data)
    analyzed = analyze(extracted)
    ranked = rank(analyzed)

    report = generate_report(ranked)
    print(report)

if __name__ == "__main__":
    run("Midfielder")
