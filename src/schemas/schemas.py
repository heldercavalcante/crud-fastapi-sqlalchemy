from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    #my_products: List[Product]
    #my_sales: List[Order]
    #my_requests: List[Order]

class Product(BaseModel):
    id: Optional[str] = None
    #user: User
    name: str
    details: str
    price: float
    available: bool = False

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    quantity: int
    delivery: bool = True
    address: str
    comments: Optional[str] = 'Sem Observações'