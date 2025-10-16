from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, database

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/buses")
def get_buses(db: Session = Depends(get_db)):
    return db.query(models.Bus).all()

@router.post("/buses")
def add_bus(name: str, route: str, db: Session = Depends(get_db)):
    new_bus = models.Bus(name=name, route=route)
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
    return new_bus
