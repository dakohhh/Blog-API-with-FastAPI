import os
import jwt
import datetime
from dotenv import load_dotenv
from model.models import TokenData
from exceptions.custom_execption import CredentialsException

load_dotenv()




def create_access_token(data):
    token = jwt.encode(
        {"user":data, 
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
        }, os.getenv("ADMIN_SECRET_KEY"))
    
    return token




def verify_access_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, os.getenv("ADMIN_SECRET_KEY"), algorithms=os.getenv("ALGORITHM"))
        return TokenData(email =payload["user"])
    except:
        raise credentials_exception