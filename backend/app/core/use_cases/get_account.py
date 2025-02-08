from fastapi import HTTPException

from backend.app.core.entities.stock import Stock


def get_account(stock: Stock,friend_name: str):
    friend = next((f for f in stock.friends if f.name.lower() == friend_name.lower()), None)
    if not friend:
        raise HTTPException(status_code=404, detail=f"Friend '{friend_name}' not found.")

    total_account = sum(order.quantity * order.price for order in friend.orders)

    return {
        "name": friend.name,
        "total_account": total_account,
        "orders": friend.orders,
    }
