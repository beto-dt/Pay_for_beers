from pydantic import BaseModel
from datetime import datetime
from typing import List

class OrderItem(BaseModel):
    name: str
    quantity: int
    price_per_unit: int = 0
    total: int = 0

class OrderRound(BaseModel):
    created: datetime
    items: List[OrderItem]


class Order(BaseModel):
    created: datetime
    paid: bool = False
    subtotal: int = 0
    taxes: int = 0
    discount: int = 0
    items: List[OrderItem]
    rounds: List[OrderRound]