from typing import Optional
from pydantic import BaseModel






class User(BaseModel):
    fullname:str
    email: str
    password:str


class Blog(BaseModel):
    title: str
    body:str



class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    email: Optional[str] =None



class User_d(BaseModel):
    email:str