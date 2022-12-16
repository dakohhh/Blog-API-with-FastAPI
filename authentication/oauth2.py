from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from exceptions.custom_execption import CredentialsException
from .token import verify_access_token





oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")




async def get_current_user(data:str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )
    
    return verify_access_token(data, credentials_exception)