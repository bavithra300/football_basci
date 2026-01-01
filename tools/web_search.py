import requests
from bs4 import BeautifulSoup

def search_players(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    text_data = soup.get_text()
    return text_data[:5000]  # limit noise
