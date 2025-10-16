from pydantic import BaseModel

# Input data (when creating a bus)
class BusCreate(BaseModel):
    route: str
    driver: str
    capacity: int

# Output data (when reading from database)
class Bus(BusCreate):
    id: int

    class Config:
        orm_mode = True
