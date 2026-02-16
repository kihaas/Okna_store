from fastapi import Request, APIRouter, Depends
from sqlalchemy.orm import Session

from ..deps import get_current_admin
from ...database import get_db
from ...crud.windows import get_windows
from .....frontend import templates

router = APIRouter()

@router.get("/admin/windows")
def list_windows(
    request: Request,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)  # admin не используется, но проверяет аутентификацию
):
    windows = get_windows(db)
    return templates.TemplateResponse(
        "admin/windows_list.html",
        {"request": request, "windows": windows}
    )