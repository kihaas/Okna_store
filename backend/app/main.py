from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates

from .routers.public import main as public_main
from .routers.public import catalog as public_catalog
from .routers.public.main import router
from ...frontend import templates

router = APIRouter()  # 👈 вот это есть?
templates = Jinja2Templates(directory="frontend/templates")

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})