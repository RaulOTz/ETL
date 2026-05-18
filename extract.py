import requests

URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


def extract_data():
    res = requests.get(URL)

    if res.status_code != 200:
        raise Exception("Error extracting data ")
    return res.json()

# Expected result: {"symbol": "BTCUSDT", "price": "65000.12"}