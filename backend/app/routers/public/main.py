from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates

from backend import app

router = APIRouter()

templates = Jinja2Templates(directory="frontend/templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
