from pydantic import BaseModel
from datetime import datetime
from typing import List

class Beer(BaseModel):
    name: str
    price: int
    quantity: int

class Friend(BaseModel):
    name: str
    orders: List[Beer]

class Stock(BaseModel):
    last_update: datetime
    beers: List[Beer]
    friends: List[Friend]