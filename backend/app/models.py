from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Window(Base):
    __tablename__ = "windows"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    type = Column(String, index=True)  # часто ищут по типу
    size = Column(String)
    color = Column(String)
    price = Column(Integer)  # Changed from String
    image_url = Column(String)


class OrderRequest(Base):
    __tablename__ = "order_requests"

    id = Column(Integer, primary_key=True)  # автоинкремент
    name = Column(String)
    phone = Column(String, index=True)  # поиск по телефону
    window_id = Column(Integer, index=True)  # поиск по окну
    size = Column(String)