from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models
from sqlalchemy import update, delete

class ProductRepository():

    def __init__(self, session:Session):
        self.session = session


    def create(self, product: schemas.Product):
        #turn schema to model
        #then the product can operate with database
        db_product = models.Product(name=product.name, 
                                    details=product.details,
                                    price=product.price,
                                    available=product.available,
                                    size=product.size,
                                    user_id=product.user_id)
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return db_product

    
    def list(self):
        products = self.session.query(models.Product).all()
        return products

    def remove(self, id: int):
        delete_product = delete(models.Product).where(models.Product.id == id)
        self.session.execute(delete_product)
        self.session.commit()


    def update(self,id:int, product: schemas.Product):
        update_product = update(models.Product).where(
                models.Product.id == id).values(name=product.name, 
                                                        details=product.details,
                                                        price=product.price,
                                                        available=product.available,
                                                        size=product.size
                                                        )
        self.session.execute(update_product)
        self.session.commit()