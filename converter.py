from os import getenv 
import requests
from fastapi import HTTPException
import aiohttp

ALPHA_VANTAGE_API_KEY= getenv("ALPHA_VANTAGE_API_KEY")


def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHA_VANTAGE_API_KEY}'
    
    try:
        response = requests.get(url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    data = response.json()
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail=data)

    exchange_rate = float(data['Realtime Currency Exchange Rate']["5. Exchange Rate"])
    return {to_currency: price * exchange_rate}

async def async_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHA_VANTAGE_API_KEY}'
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
                
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail=data)

    exchange_rate = float(data['Realtime Currency Exchange Rate']["5. Exchange Rate"])
    return {to_currency: price * exchange_rate}