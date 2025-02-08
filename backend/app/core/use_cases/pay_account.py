from fastapi import HTTPException

from backend.app.core.entities.stock import Stock


def pay_account(stock: Stock, split_equally: bool, friend_name: str = None):
    if split_equally:
        total_account = sum(
            order.quantity * order.price for friend in stock.friends for order in friend.orders
        )

        split_amount = total_account / len(stock.friends)

        return {
            "message": "El total se ha dividido entre los amigos",
            "split_amount_per_friend": split_amount,
        }
    else:
        if not friend_name:
            raise HTTPException(
                status_code=400, detail="Debe especificar el nombre del amigo si no se divide equitativamente."
            )

        friend = next(
            (f for f in stock.friends if f.name.lower() == friend_name.lower()), None
        )

        if not friend:
            raise HTTPException(
                status_code=404, detail=f"Amigo '{friend_name}' no encontrado."
            )

        total_account = sum(order.quantity * order.price for order in friend.orders)
        return {
            "message": f"El amigo {friend.name} debe pagar un total de {total_account:.2f}",
            "total_account": total_account,
            "orders": [{"name": order.name, "quantity": order.quantity, "price": order.price} for order in
                       friend.orders],
        }
