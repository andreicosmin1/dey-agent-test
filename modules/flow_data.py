import requests
from typing import Tuple

def run(token: str, ticker: str) -> Tuple[int, str]:
    url = f"https://api.unusualwhales.com/api/historic_chains/{ticker}?limit=100"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return 0, f"[FlowData] Eroare {response.status_code} la accesarea API."

        json_data = response.json()

        if isinstance(json_data, dict) and "data" in json_data:
            options_data = json_data["data"]
        elif isinstance(json_data, list):
            options_data = json_data
        else:
            return 0, "[FlowData] Format necunoscut în răspunsul API."

        bullish = sum(1 for opt in options_data if opt.get("direction") == "bullish")
        bearish = sum(1 for opt in options_data if opt.get("direction") == "bearish")

        score = bullish - bearish
        interpretation = f"[FlowData] Score: {score} | Bullish: {bullish} | Bearish: {bearish}"

        return score, interpretation

    except Exception as e:
        return 0, f"[FlowData] Eroare la procesare: {str(e)}"

