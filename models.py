from sqlalchemy import Column, Integer, String
from .database import Base

class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    route = Column(String, index=True)
    driver = Column(String)
    capacity = Column(Integer)

