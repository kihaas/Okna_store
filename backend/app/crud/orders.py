from sqlalchemy.orm import Session
from ..models import OrderRequest


def create_order(db:Session, order_data):
    db_order = OrderRequest(**order_data.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order