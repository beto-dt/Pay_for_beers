from datetime import datetime

from backend.app.core.entities.stock import Stock, Beer, Friend

BASE_DATE = datetime(2024, 9, 10, 12, 0, 0)

stock_data = Stock(
    last_update=datetime(2024, 9, 10, 12, 0, 0),
    beers=[
        Beer(name="Corona", price=115, quantity=5),
        Beer(name="Quilmes", price=120, quantity=2),
        Beer(name="Club Colombia", price=110, quantity=3),
    ],
    friends=[
        Friend(name="Juan", orders=[Beer(name="Corona", price=115, quantity=2)]),
        Friend(name="Pedro", orders=[Beer(name="Quilmes", price=120, quantity=1)]),
        Friend(name="Maria", orders=[Beer(name="Club Colombia", price=110, quantity=1)]),
    ]
)
