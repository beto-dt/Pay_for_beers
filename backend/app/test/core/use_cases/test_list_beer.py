from backend.app.core.entities.stock import Stock, Beer
from backend.app.core.use_cases.list_beer import list_beer
from datetime import datetime, timezone


def test_list_beer_with_non_zero_quantity():
    beers = [
        Beer(name="IPA", quantity=10, price=599),
        Beer(name="Stout", quantity=5, price=649),
        Beer(name="Pilsner", quantity=0, price=499)
    ]

    stock = Stock(
        last_update=datetime.now(timezone.utc),
        beers=beers,
        friends=[]
    )

    result = list_beer(stock)

    assert len(result) == 2
    assert all(beer.quantity > 0 for beer in result)
    assert result[0].name == "IPA"
    assert result[1].name == "Stout"


def test_list_beer_with_no_stock():
    stock = Stock(
        last_update=datetime.now(timezone.utc),
        beers=[],
        friends=[]
    )

    result = list_beer(stock)

    assert result == []


def test_list_beer_all_zero_quantity():
    beers = [
        Beer(name="Lager", quantity=0,price=599),
        Beer(name="Ale", quantity=0,price=599),
        Beer(name="Porter", quantity=0,price=599)
    ]

    stock = Stock(
        last_update=datetime.now(timezone.utc),
        beers=beers,
        friends=[]
    )

    result = list_beer(stock)

    assert result == []
