from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ...database import get_db
import crud


router = APIRouter()
templates = Jinja2Templates(directory="frontrend/templates")


@router.get("/catalog")
def catalog(request: Request, db: Session = Depends(get_db)):
    windows = crud.get_windows(db)
    return templates.TemplateResponse(
        "catalog.html",
        {"request": request, "windows": windows}
    )
