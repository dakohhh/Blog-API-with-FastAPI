from sqlalchemy.orm import Session
from database.database import SessionLocal
from database.schema import User as user_table
from model.models import User
from authentication.hashing import hashPassword, checkPassword



async def create_user(user:User,db:Session):
    

    new_user = user_table(full_name=user.fullname,email=user.email,password = hashPassword(user.password))
    
    db.add(new_user)

    db.commit()

    db.refresh(new_user)



def does_email_exist(email:str,db:Session):
    
    result = db.query(user_table).filter(user_table.email == email).first()

    if result:
        return True
    
def auth_user(email, password, db:Session):
    user = db.query(user_table).filter(user_table.email == email).first()

    if checkPassword(password, user.password):
        return True

