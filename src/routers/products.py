from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from schemas import schemas
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repository.product import ProductRepository


router = APIRouter()


@router.post("/products")
def create_products(product: schemas.Product, session:Session = Depends(get_db)):
    product_created = ProductRepository(session).create(product)
    return product_created


@router.get("/products")
def product_list(session:Session = Depends(get_db)):
    products = ProductRepository(session).list()
    return products


@router.put("/products/{id}")
def update_products(id:int, product: schemas.Product, session:Session = Depends(get_db)):
    ProductRepository(session).update(id, product)
    return {"msg":"product updated successfully"}


@router.delete("/products/{id}")
def remove_products(id:int, session:Session = Depends(get_db)):
    ProductRepository(session).remove(id)
    return {"msg": "product removed successfully"}