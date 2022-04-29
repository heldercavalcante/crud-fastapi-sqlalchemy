from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from schemas import schemas
from infra.sqlalchemy.config.database import get_db, create_db
from infra.sqlalchemy.repository.product import ProductRepository

create_db()
app = FastAPI()


@app.post("/products")
def create_products(product: schemas.Product, db:Session = Depends(get_db)):
    product_created = ProductRepository(db).create(product)
    return product_created


@app.get("/products")
def product_list(db:Session = Depends(get_db)):
    products = ProductRepository(db).list()
    return products