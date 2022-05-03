from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str
    password: str
    #my_products: List[Product] = []
    #my_sales: List[Order]
    #my_requests: List[Order]
    class Config:
        orm_mode = True




class Product(BaseModel):
    id: Optional[int] = None
    #user: User
    name: str
    details: str
    price: float
    available: bool = False
    size: float
    user_id: Optional[int]

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: str
    details: str
    price: float
    available: bool = False
    size: float
    user_id: Optional[int]

    class Config:
        orm_mode = True




# class Order(BaseModel):
#     id: Optional[int] = None
#     user: User
#     product: Product
#     quantity: int
#     delivery: bool = True
#     address: str
#     comments: Optional[str] = 'Sem Observações'