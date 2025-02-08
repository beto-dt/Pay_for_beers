from fastapi import APIRouter, HTTPException

from backend.app.core.entities.order import Order
from backend.app.core.use_cases.get_account import get_account
from backend.app.core.use_cases.list_beer import list_beer
from backend.app.core.use_cases.list_friend import list_friend
from backend.app.core.use_cases.pay_account import pay_account
from backend.app.core.use_cases.place_order import place_order
from backend.app.infrastructure.storage import stock_data

router = APIRouter()


@router.get("/beers")
def list_beers_route():
    return list_beer(stock_data)


@router.get("/friends")
def list_beers_route():
    return list_friend(stock_data)


@router.get("/account/{friend_name}")
def get_account_route(friend_name: str):
    return get_account(stock_data, friend_name)


@router.post("/order")
def receive_order(order: Order):
    try:
        result = place_order(stock_data, order.friend_name, order.beer_name, order.quantity)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/pay_account")
def pay_account_route(split_equally: bool, friend_name: str):
    return pay_account(stock_data, split_equally, friend_name)
