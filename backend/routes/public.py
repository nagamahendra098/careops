from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Message

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/public_reply")
def public_reply(conversation_id: int, content: str, db: Session = Depends(get_db)):
    msg = Message(
        conversation_id=conversation_id,
        sender="customer",
        content=content
    )
    db.add(msg)
    db.commit()
    return {"status": "sent"}
