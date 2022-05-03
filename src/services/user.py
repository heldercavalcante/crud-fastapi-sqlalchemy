from infra.sqlalchemy.repository.user import UserRepository
from schemas import schemas
from sqlalchemy.orm import Session
from infra.sqlalchemy.models import models
from sqlalchemy import select, update, delete


class UserService:
    
    def __init__(self, repository:UserRepository):
        self.repository = repository


    def create(self, user: schemas.User):
        user = models.User(name=user.name,
                              password=user.password,
                              phone=user.phone
                                )
        self.repository.create(user)
        return user

    def list(self):    
        return self.repository.list()

    def remove(self, id: int):
        product_to_delete = self.repository.get_by_id(id)
        self.repository.remove(product_to_delete)


    def update(self,id:int, user: schemas.User):
        user_model = self.repository.get_by_id(id)
        user_model.name = user.name
        user_model.password = user.password
        user_model.phone = user.phone
        self.repository.update(user_model)
        return user_model
