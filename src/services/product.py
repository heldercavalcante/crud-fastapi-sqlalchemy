import time
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
                                    user_id=product.user_id)
        
        product.validate()
        self.repository.create(product)
        return product

    
    # def list(self):
    #     #time.sleep(3)
    #     return self.repository.list()
  

    def remove(self, id: int):
        product = self.repository.get_by_id(id)
        self.repository.remove(product)



    def update(self,id:int, product: schemas.Product):
        product_model = self.repository.get_by_id(id)
        product_model.name = product.name 
        product_model.details=product.details
        product_model.price=product.price
        product_model.available=product.available
        self.repository.update(product_model)
        return product_model

    def get_by_id(self,id):
        return self.repository.get_by_id(id)


    def list(self, start, end, page_size, page_num):

        products = self.repository.list()

        response = {
        "data":products[start:end],
        "total":len(products),
        "count":page_size,
        "pagination": {}
    }
        if end >= len(products):
            response["pagination"]["next"] = None

            if page_num > 1:
                response["pagination"]["previous"] = f'/products?page_num={page_num-1}&page_size={page_size}'
            else:
                response["pagination"]["previous"] = None
        else:
            if page_num > 1:
                response["pagination"]["previous"] = f'/products?page_num={page_num-1}&page_size={page_size}'
            else:
                response["pagination"]["previous"] = None   

            response["pagination"]["next"] = f'/products?page_num={page_num+1}&page_size={page_size}'  
        return response


    def list_by_interval(self, start, end, page_size, page_num):
        products = self.repository.list_by_interval(start,end)
        number_of_registres = self.repository.get_number_of_registry()

        response = {
        "data":products,
        "total":number_of_registres,
        "count":page_size,
        "pagination": {}
    }
        if end >= number_of_registres:
            response["pagination"]["next"] = None

            if page_num > 1:
                response["pagination"]["previous"] = f'/products?page_num={page_num-1}&page_size={page_size}'
            else:
                response["pagination"]["previous"] = None
        else:
            if page_num > 1:
                response["pagination"]["previous"] = f'/products?page_num={page_num-1}&page_size={page_size}'
            else:
                response["pagination"]["previous"] = None   

            response["pagination"]["next"] = f'/products?page_num={page_num+1}&page_size={page_size}'  
        return response

    # def get_number_of_registres(self):
    #     return self.repository.get_number_of_registres()

    def list_test(self):
        return self.repository.list()


        #test of pagination

    def get_by_interval(self, params):
        return self.repository.get_by_interval(params)

    def filter_by_param(self, params):
        print(f'aqui está o resultado{self.repository.filter_by_param(params)}')
        return self.repository.filter_by_param(params)