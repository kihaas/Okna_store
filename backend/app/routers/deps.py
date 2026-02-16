from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db as get_db_session
import os
from dotenv import load_dotenv

load_dotenv()

security = HTTPBasic()

def get_current_admin(credentails: HTTPBasicCredentials = Depends(security)):
    admin_username = os.getenv('ADMIN_USERNAME', "admin")
    admin_password = os.getenv('ADMIN_PASSWORD', "secret")

    if credentails.username != admin_username or credentails.password != admin_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Basic"}
        )
    return credentails.username

