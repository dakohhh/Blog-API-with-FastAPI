from fastapi import FastAPI

from routers.user import user
from routers.login import auth
from routers.blogs import blog
from database.schema import Base
from database.database import SessionLocal, engine
from exceptions.custom_execption import *

Base.metadata.create_all(bind=engine)




app = FastAPI()

app.include_router(user)
app.include_router(auth)
app.include_router(blog)
app.add_exception_handler(UserExistExecption, user_exist_exception_handler)
app.add_exception_handler(UnauthorizedExecption, unauthorized_exception_handler)
app.add_exception_handler(ServerErrorException, server_exception_handler)
app.add_exception_handler(NotFoundError, not_found)
app.add_exception_handler(CredentialsException, credentail_exception_handler)



@app.get("/api")
def main():
    return {"msg" :"Welcome to the blog api"}
