from gemini_client import get_model

def coach_agent(position):
    model = get_model()

    prompt = f"""
    You are an elite football AI coach.

    Position needed: {position}

    Do the following:
    1. Decide web search keywords
    2. Decide key performance metrics
    3. Decide how players should be ranked

    Respond ONLY in bullet points.
    """

    response = model.generate_content(prompt)
    return response.text
