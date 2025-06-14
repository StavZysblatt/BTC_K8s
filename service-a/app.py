import os

from fastapi import FastAPI

#tm-55817ef9-89b4-4311-90d8-e6f333f37e45
import requests
import asyncio

app = FastAPI(root_path="/")
btc_prices = []

API_KEY = os.getenv("TOKEN_METRICS_API_KEY")
URL = "https://api.tokenmetrics.com/v2/price?token_id=3375"
HEADERS = {"x-api-key": API_KEY}

async def fetch_prices():
    while True:
        try:
            response = requests.get(URL,headers=HEADERS)
            data = response.json()
            price = data["data"][0]["CURRENT_PRICE"]

            btc_prices.append(price)
            if len(btc_prices) >60:
                btc_prices.pop(0)

            print(f"Fetched BTC price {price}")
        except Exception as e:
            print("Error fetching price:", e)

        await asyncio.sleep(60)

@app.on_event("startup")
async def start_fetching():
    asyncio.create_task(fetch_prices())

@app.get("/price")
def get_price():
    if not btc_prices:
        return{"error":"Price data not available"}

    current = btc_prices[-1]
    average = sum(btc_prices) / len(btc_prices)

    return {
        "current_price": round(current, 2),
        "average":round(average, 2)
    }
