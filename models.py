from sqlalchemy import Column, INTEGER, VARCHAR, DATETIME, TEXT
from pydantic import BaseModel

from db import Base
from db import ENGINE

class DBTable(Base):
    __tablename__ = 'bb'
    id          = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    title       = Column(VARCHAR(45), nullable=True)
    time        = Column(DATETIME(6), nullable=True)
    contents    = Column(TEXT, nullable=True)

class Data(BaseModel):
    title   : str
    contents: str