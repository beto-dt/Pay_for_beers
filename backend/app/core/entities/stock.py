from pydantic import BaseModel
from datetime import datetime
from typing import List

class Beer(BaseModel):
    name: str
    price: int
    quantity: int

class Stock(BaseModel):
    last_update: datetime
    beers: List[Beer]