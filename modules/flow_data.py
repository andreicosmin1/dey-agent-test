import requests

def get_flow_score(token: str, ticker: str) -> tuple[int, str]:
    url = f"https://api.unusualwhales.com/api/historic_chains/{ticker}?limit=100"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Exemplu: scor simplificat
        bullish = sum(1 for opt in data if opt.get("direction") == "bullish")
        bearish = sum(1 for opt in data if opt.get("direction") == "bearish")

        score = bullish - bearish
        interpretation = f"Flow Score: {score} | Bullish: {bullish}, Bearish: {bearish}"
        return score, interpretation

    except Exception as e:
        return 0, f"Error fetching flow data: {e}"

