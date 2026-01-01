import google.generativeai as genai

def coach_agent(position):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
You are an AI football coach.

User requested players for position: {position}

Your task:
1. Decide search keywords
2. Decide important metrics for a coach
3. Guide tools to fetch and analyze data

Return only clear instructions.
"""

    response = model.generate_content(prompt)
    return response.text
