from asyncio import gather
from fastapi import APIRouter
from converter import sync_converter, async_converter

router = APIRouter()

# url?to_currency=USD,EUR,GBP&price=5.55
@router.get("/converter/{from_currency}")
def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(",")
    
    result = []
    
    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        
        result.append(response)
        
    return result

@router.get("/async/converter/{from_currency}")
async def async_converter_router(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(",")
    
    coroutines = []
    
    for currency in to_currencies:
        coro = async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        
        coroutines.append(coro)
        
    result = await gather(*coroutines)
    return result