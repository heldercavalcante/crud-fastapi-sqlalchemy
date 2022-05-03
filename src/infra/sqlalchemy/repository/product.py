from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models
from sqlalchemy import update, delete

class ProductRepository():

    def __init__(self, session:Session):
        self.session = session


    def create(self, product: models.Product):
        #turn schema to model
        #then the product can operate with database    
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    
    def list(self):
        return self.session.query(models.Product).all()
        

    def remove(self, product:models.Product):
        delete_product = delete(models.Product).where(models.Product.id == product.id)
        self.session.execute(delete_product)
        self.session.commit()


    def update(self, product: models.Product):
        db_product = update(models.Product).where(
                models.Product.id == product.id).values(name=product.name, 
                                                        details=product.details,
                                                        price=product.price,
                                                        available=product.available,
                                                        size=product.size
                                                        )
        self.session.execute(db_product)
        self.session.commit()
        return product

    def get_by_id(self, id: int) -> models.Product:
        return self.session.query(models.Product).where(models.Product.id == id).first()
