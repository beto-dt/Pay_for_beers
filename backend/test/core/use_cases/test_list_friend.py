import pytest
from backend.app.core.entities.stock import Stock, Friend
from backend.app.core.entities.order import Order
from backend.app.core.use_cases.list_friend import list_friend


def test_list_friend():
    # Datos de prueba
    stock = Stock(
        friends=[
            Friend(name="Alice", orders=[Order(item="Pizza", quantity=2, price=10.0)]),
            Friend(name="Bob", orders=[Order(item="Soda", quantity=3, price=2.5)]),
            Friend(name="Charlie", orders=[Order(item="Burger", quantity=1, price=8.0)]),
        ]
    )

    # Llamar a la función
    result = list_friend(stock)

    # Validar el resultado
    assert len(result) == 3  # Debe devolver 3 amigos
    assert result[0].name == "Alice"
    assert result[1].name == "Bob"
    assert result[2].name == "Charlie"