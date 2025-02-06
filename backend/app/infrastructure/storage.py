from datetime import datetime
from backend.app.core.entities.stock import Stock
from backend.app.core.entities.order import Order, OrderItem, OrderRound

BASE_DATE = datetime(2024, 9, 10, 12, 0, 0)

stock_data = Stock(
    last_update=datetime(2024, 9, 10, 12, 0, 0),
    beers=[
        {"name": "Corona", "price": 115, "quantity": 5},
        {"name": "Quilmes", "price": 120, "quantity": 1},
        {"name": "Club Colombia", "price": 110, "quantity": 3}
    ]
)

order_data = Order(
    created=BASE_DATE.replace(minute=0, second=30),
    items=[
        OrderItem(name="Corona", quantity=2),
        OrderItem(name="Club Colombia", quantity=1),
        OrderItem(name="Quilmes", quantity=1),
    ],
    rounds=[
        OrderRound(
            created=BASE_DATE.replace(minute=20),
            items=[
                OrderItem(name="Corona", quantity=2),
                OrderItem(name="Club Colombia", quantity=1),
            ],
        ),
        OrderRound(
            created=datetime(2024, 9, 10, 12, 20, 0),
            items=[
                OrderItem(name="Club Colombia", quantity=1),
                OrderItem(name="Quilmes", quantity=1),
            ],
        ),
    ],
)