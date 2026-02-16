from fastapi import Depends, APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")
security = HTTPBasic()

@router.get("/admin/login")
def login_form(request: Request):
    return templates.TemplateResponse("admin/login.html", {"request": request})


@router.post("/admin/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    return {"message": "Успешный вход"}

@router.get("/admin/logout")
def logout():
    return {"messsage": "Выход выполнен"}