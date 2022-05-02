from schemas import schemas
from requests import Session
from infra.sqlalchemy.models import models
from sqlalchemy import select, update, delete


class UserRepository:
    
    def __init__(self, session:Session):
        self.session = session

    
    def create(self, user: schemas.User):
        db_user = models.User(name=user.name,
                              password=user.password,
                              phone=user.phone
                                )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def list(self):
        #users = self.session.query(models.User).all()
        select_user = select(models.User)
        users = self.session.execute(select_user).all()    
        return users

    def remove(self, id: int):
        delete_user = delete(models.User).where(models.User.id == id)
        self.session.execute(delete_user)
        self.session.commit()

    def update(self,id:int, user: schemas.User):
        update_user = update(models.User).where(
                models.User.id == id).values(name=user.name, 
                                                        password=user.password,
                                                        phone=user.phone
                                                        )
        self.session.execute(update_user)
        self.session.commit()
