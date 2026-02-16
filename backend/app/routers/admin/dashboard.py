from fastapi import Depends, APIRouter, HTTPException, Request
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates

from backend.app.routers.deps import get_current_admin
from ..deps import get_current_admin

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")

@router.get("/admin")
def admin_dashboard(request: Request, current_user=Depends(get_current_admin)):
    return templates.TemplateResponse(
        "admin/dashboard.html",
        {"request": request}
    )