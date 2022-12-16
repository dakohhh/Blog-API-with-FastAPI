from fastapi import APIRouter, status, Depends
from model.models import User
from response.response import customResponse
from sqlalchemy.orm import Session
from database.database import SessionLocal, get_db
from database.crud import create_user, does_email_exist
from exceptions.custom_execption import UserExistExecption



user = APIRouter(
    prefix="/api",
    tags=["Users"]
)



@user.post("/signup")
async def signup(user: User, db:Session=Depends(get_db)):

    if await does_email_exist(user.email, db):
        raise UserExistExecption("Email already exist")
    
    print(user.email)

    await create_user(user, db)

    return customResponse(status.HTTP_201_CREATED, "Account created")
