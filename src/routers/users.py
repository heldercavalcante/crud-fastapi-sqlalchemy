from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from schemas import schemas
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repository.user import UserRepository


router = APIRouter()


@router.post("/users")
def create_user(user: schemas.User, session:Session = Depends(get_db)):
    user_created = UserRepository(session).create(user)
    return user_created


@router.get("/users")
def user_list(session:Session = Depends(get_db)):
    users = UserRepository(session).list()
    return users

@router.put("/users/{id}")
def update_user(id:int, user: schemas.User, session:Session = Depends(get_db)):
    UserRepository(session).update(id, user)
    return {"msg":"User updated successfully"}


@router.delete("/users/{id}")
def remove_user(id:int, session:Session = Depends(get_db)):
    UserRepository(session).remove(id)
    return {"msg": "User removed successfully"}
