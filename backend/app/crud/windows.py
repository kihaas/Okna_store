from sqlalchemy.orm import Session
from ..models import Window

def get_windows(db: Session):
    return db.query(Window).all()