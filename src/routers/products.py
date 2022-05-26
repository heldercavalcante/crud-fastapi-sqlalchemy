from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from schemas import schemas
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repository.product import ProductRepository
from services.product import ProductService

#importing of patination atributs
from fastapi_pagination import Page, add_pagination, LimitOffsetPage, Params
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter()

# session: Session = Depends(get_db)
# repository = ProductRepository(session)
# service = ProductService(repository)


@router.post("/products")
def create_products(product: schemas.Product, session:Session = Depends(get_db)):
    #product_created = ProductRepository(session).create(product)
    product_created = ProductService(ProductRepository(session)).create(product)


    # for n in range(500000):
    #     product_created = ProductService(ProductRepository(session)).create(product)

    return product_created

@router.get("/products", response_model=Page[schemas.Product])
@router.get("/products/limit-offset", response_model=LimitOffsetPage[schemas.Product])
async def product_list(params: Params = Depends(),session:Session = Depends(get_db)):
    return ProductService(ProductRepository(session)).get_by_interval(params)

#############################################

# @router.get("/products")
# def product_list(session:Session = Depends(get_db),page_num:int = 1, page_size:int=10):
#     start = (page_num-1) * page_size
#     end = start + page_size
#     response = ProductService(ProductRepository(session)).list_by_interval(start, end, page_size, page_num)
#     return response



@router.get("/products/{id}")
def get_product_by_id(id, session:Session = Depends(get_db)):
    return ProductService(ProductRepository(session)).get_by_id(id)

@router.get("/products/filter/{params}")
def filter_by_params(params:str, session:Session = Depends(get_db)):
    products = ProductService(ProductRepository(session)).filter_by_param(params)
    return products


@router.put("/products/{id}")
def update_products(id:int, product: schemas.ProductUpdate, session:Session = Depends(get_db)):
    ProductService(ProductRepository(session)).update(id, product)
    return {"msg":"product updated successfully"}


@router.delete("/products/{id}")
def remove_products(id:int, session:Session = Depends(get_db)):
    ProductService(ProductRepository(session)).remove(id)
    return {"msg": "product removed successfully"}



add_pagination(router)