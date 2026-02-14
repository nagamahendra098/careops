from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Contact, Booking, Message
from datetime import date

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):

    total_contacts = db.query(Contact).count()
    total_bookings = db.query(Booking).count()

    today = date.today().isoformat()

    today_bookings = db.query(Booking).filter(
        Booking.date == today
    ).count()

    total_messages = db.query(Message).count()

    return {
        "total_contacts": total_contacts,
        "total_bookings": total_bookings,
        "today_bookings": today_bookings,
        "total_messages": total_messages
    }
