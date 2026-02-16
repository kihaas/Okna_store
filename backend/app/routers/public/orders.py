from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ...database import get_db
from ... import  schemas
from ...crud.orders import create_order as create_order_crud

router = APIRouter()

@router.post("/api/order")
def create_order(order:schemas.OrderCreate, db: Session=Depends(get_db)):
    new_order = create_order(order, db)

    return {
        "status": "success",
        "order_id": new_order.id,
        "message": "Заказ создан"
    }
