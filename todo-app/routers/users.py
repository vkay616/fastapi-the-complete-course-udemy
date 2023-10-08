from fastapi import APIRouter, Depends, HTTPException, status
from models import Users
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from .auth import get_current_user
from passlib.context import CryptContext



router = APIRouter(
    prefix="/users",
    tags=["users"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


bcrypt_context = CryptContext(schemes=['bcrypt'])


db_dependency = Annotated[Session, Depends(get_db)]

user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/user", status_code=status.HTTP_200_OK)
def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    
    user_model = db.query(Users).filter(Users.username == user.get("username")).first()

    if user_model is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found!")
    
    return user_model


@router.put("/user/update", status_code=status.HTTP_202_ACCEPTED)
def update_password(user: user_dependency, db: db_dependency, new_password: str):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    
    user_model = db.query(Users).filter(Users.username == user.get("username")).first()

    if user_model is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found!")
    
    user_model.hashed_password = bcrypt_context.hash( new_password)

    db.add(user_model)

    db.commit()