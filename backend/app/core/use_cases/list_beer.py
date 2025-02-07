from backend.app.core.entities.stock import Stock

def list_beer(stock: Stock):
    return [beer for beer in stock.beers if beer.quantity > 0]