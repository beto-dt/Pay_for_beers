from backend.app.core.entities.stock import Stock


def list_friend(stock: Stock):
    return [fr for fr in stock.friends]
