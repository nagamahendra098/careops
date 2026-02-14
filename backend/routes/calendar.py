from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Booking

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/calendar")
def get_calendar(db: Session = Depends(get_db)):
    bookings = db.query(Booking).all()

    return [
        {
            "id": b.id,
            "title": f"Booking {b.id}",
            "date": b.date,
            "time": b.time,
            "contact_id": b.contact_id
        }
        for b in bookings
    ]
