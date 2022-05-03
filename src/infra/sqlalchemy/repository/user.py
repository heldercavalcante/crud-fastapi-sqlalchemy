from sqlalchemy.orm import Session
from infra.sqlalchemy.models import models
from sqlalchemy import select, update, delete


class UserRepository:
    
    def __init__(self, session:Session):
        self.session = session

    
    def create(self, user: models.User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def list(self):
        #users = self.session.query(models.User).all()
        select_user = select(models.User)
        return self.session.execute(select_user).all()    
        

    def remove(self, user: models.User):
        delete_user = delete(models.User).where(models.User.id == user.id)
        self.session.execute(delete_user)
        self.session.commit()

    def update(self, user: models.User):
        update_user = update(models.User).where(
                models.User.id == user.id).values(name=user.name, 
                                                  password=user.password,
                                                  phone=user.phone)
        self.session.execute(update_user)
        self.session.commit()

    def get_by_id(self, id:int):
        return self.session.query(models.User).where(models.User.id == id).first()
