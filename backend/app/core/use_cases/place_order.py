from backend.app.core.entities.stock import Stock

def place_order(stock: Stock, friend_name: str, beer_name: str, quantity: int):
    friend = next((f for f in stock.friends if f.name == friend_name), None)
    if not friend:
        raise ValueError(f"Friend '{friend_name}' not found.")

    beer = next((b for b in stock.beers if b.name == beer_name), None)
    if not beer:
        raise ValueError(f"Beer '{beer_name}' not found in stock.")

    if beer.quantity < quantity:
        raise Exception(f"Not enough stock for the beer '{beer_name}'.")

        beer.quantity -= quantity

        ordered_beer = beer.copy()
        ordered_beer.quantity = quantity
        friend.orders.append(ordered_beer)


    return f"{friend_name} successfully ordered {quantity} {beer_name}(s)."

