from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from database.database import get_db
from database.crud import does_email_exist, auth_user
from sqlalchemy.orm import Session
from exceptions.custom_execption import NotFoundError





auth  = APIRouter(
        prefix="", 
        tags=["Authentication"]
)



@auth.post("/login")
async def login(request:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    if not does_email_exist(request.username, db):
        raise NotFoundError("Invalid Credentails")
    
    if not auth_user(request.username, request.password, db):
        raise NotFoundError("Invalid Credrntails")


    from  authentication.token import create_access_token

    access_token = create_access_token(request.username)

    return {"access_token": access_token, "token_type": "bearer"}