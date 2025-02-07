from pydantic import BaseModel
class Order(BaseModel):
    friend_name: str
    beer_name: str
    quantity: int

