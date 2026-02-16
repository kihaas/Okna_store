from pydantic import BaseModel, Field
from typing import Optional

class OrderCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description='Имя клиента')
    phone: str = Field(..., min_length=12, description="Телефон в формате +7")
    window_id: Optional[int] = Field(None, description="ID выбранного окна")
    size: Optional[str] = Field(None, description="Желаемый размер окна")