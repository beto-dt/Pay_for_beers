from fastapi import APIRouter
from backend.app.core.use_cases.list_beer import list_beer
from backend.app.infrastructure.storage import stock_data
router = APIRouter()

@router.get("/beers")
def list_beers_route():
    return list_beer(stock_data);
