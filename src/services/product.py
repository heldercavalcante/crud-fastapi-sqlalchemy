
from infra.sqlalchemy.repository.product import ProductRepository
from infra.sqlalchemy.models import models
from schemas import schemas

class ProductService():

    def __init__(self, repository: ProductRepository):
        self.repository = repository


    def create(self, product: schemas.Product):
        #turn schema to model
        #then the product can operate with database
        product = models.Product(name=product.name, 
                                    details=product.details,
                                    price=product.price,
                                    available=product.available,
                                    size=product.size,
                                    user_id=product.user_id)
        
        product.validate()
        self.repository.create(product)
        return product

    
    def list(self):
        return self.repository.list()
  

    def remove(self, id: int):
        product = self.repository.get_by_id(id)
        self.repository.remove(product)



    def update(self,id:int, product: schemas.Product):
        product_model = self.repository.get_by_id(id)
        product_model.name = product.name 
        product_model.details=product.details
        product_model.price=product.price
        product_model.available=product.available
        product_model.size=product.size
        self.repository.update(product_model)
        return product_model
