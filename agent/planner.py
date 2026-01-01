def plan_tools(position):
    return {
        "search_query": f"top {position} football players stats wins losses age fitness",
        "expected_metrics": [
            "age", "matches won", "matches lost",
            "fitness", "performance rating"
        ]
    }
