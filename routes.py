from fastapi import APIRouter
from converter import sync_converter

router = APIRouter()

# url?to_currency=USD,EUR,GBP&price=5.55
@router.get("/converter/{from_currency}")
def converter(from_currency: str, to_correncies: str, price: float):
    to_correncies = to_correncies.split(",")
    
    result = []
    
    for currency in to_correncies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        
        result.append(response)
        
    return result