from sqlalchemy.orm import Session
from . import models, schemas

# Create a new bus
def create_bus(db: Session, bus: schemas.BusCreate):
    db_bus = models.Bus(route=bus.route, driver=bus.driver, capacity=bus.capacity)
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus

# Get all buses
def get_buses(db: Session):
    return db.query(models.Bus).all()
