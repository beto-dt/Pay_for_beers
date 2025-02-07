from datetime import datetime
from backend.app.core.entities.stock import Stock

def update_stock(stock: Stock, beer_name: str, quantity: int):
    beer = next((b for b in stock.beers if b["name"] == beer_name), None)
    if not beer:
        raise Exception(f"Beer '{beer_name}' not found in stock.")

    if beer["quantity"] + quantity < 0:
        raise Exception(
            f"Not enough stock for '{beer_name}'. "
            f"Current stock: {beer['quantity']}, tried to deduct: {abs(quantity)}"
        )

    beer["quantity"] += quantity

    stock.last_update = datetime.now()
