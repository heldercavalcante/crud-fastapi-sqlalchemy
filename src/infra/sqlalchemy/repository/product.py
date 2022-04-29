from statistics import mode
from unicodedata import name
from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models

class ProductRepository():

    def __init__(self, db:Session):
        self.db = db


    def create(self, product: schemas.Product):
        #turn schema to model
        #then the product can operate with database
        db_product = models.Product(name=product.name, 
                                    details=product.details,
                                    price=product.price,
                                    available=product.available)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    
    def list(self):
        products = self.db.query(models.Product).all()
        return products

    def remove(self):
        pass

    def get(self):
        pass