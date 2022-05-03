from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from schemas import schemas
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repository.product import ProductRepository
from services.product import ProductService



router = APIRouter()

# session: Session = Depends(get_db)
# repository = ProductRepository(session)
# service = ProductService(repository)


@router.post("/products")
def create_products(product: schemas.Product, session:Session = Depends(get_db)):
    #product_created = ProductRepository(session).create(product)
    product_created = ProductService(ProductRepository(session)).create(product)
    return product_created


@router.get("/products")
def product_list(session:Session = Depends(get_db)):
    #return ProductRepository(session).list()
    return ProductService(ProductRepository(session).list())



@router.put("/products/{id}")
def update_products(id:int, product: schemas.ProductUpdate, session:Session = Depends(get_db)):
    ProductService(ProductRepository(session)).update(id, product)
    return {"msg":"product updated successfully"}


@router.delete("/products/{id}")
def remove_products(id:int, session:Session = Depends(get_db)):
    ProductService(ProductRepository(session)).remove(id)
    return {"msg": "product removed successfully"}