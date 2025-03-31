from asyncio import gather
from fastapi import APIRouter, Path, Query
from converter import sync_converter, async_converter
from schamas import ConverterInput

router = APIRouter()

# url?to_currency=USD,EUR,GBP&price=5.55
@router.get("/converter/{from_currency}")
def converter(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"), 
    to_currencies: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$"), 
    price: float = Query(gt=0)
):
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
async def async_converter_router(
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"), 
    to_currencies: str = Query(max_length=50, regex="^[A-Z]{3}(,[A-Z]{3})*$"), 
    price: float = Query(gt=0)
):
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


@router.get("/v2/converter/{from_currency}")
def converter(
    body: ConverterInput,
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
):
    to_currencies = body.to_currencies
    price = body.price
    
    result = []
    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        
        result.append(response)
        
    return result


@router.get("/v2/async/converter/{from_currency}")
def converter(
    body: ConverterInput,
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
):
    to_currencies = body.to_currencies
    price = body.price
    
    result = []
    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        
        result.append(response)
        
    return result