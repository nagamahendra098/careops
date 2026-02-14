from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Booking, Message, Conversation

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/booking")
def create_booking(contact_id: int, date: str, time: str, db: Session = Depends(get_db)):

    booking = Booking(
        contact_id=contact_id,
        date=date,
        time=time,
        status="scheduled"
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)

    # find conversation
    convo = db.query(Conversation).filter(
        Conversation.contact_id == contact_id
    ).first()

    if convo:
        msg = Message(
            conversation_id=convo.id,
            sender="system",
            content=f"Booking confirmed for {date} at {time}"
        )
        db.add(msg)
        db.commit()

    return booking
