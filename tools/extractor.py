import google.generativeai as genai

def extract_player_stats(raw_text, position):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
From the text below, extract football players who are {position}.
For each player return:
- Name
- Age
- Wins
- Losses
- Fitness level
- Overall rating

Text:
{raw_text}
"""

    response = model.generate_content(prompt)
    return response.text
