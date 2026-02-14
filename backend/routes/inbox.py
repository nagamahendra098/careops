from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Conversation, Message

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get all conversations
@router.get("/conversations")
def get_conversations(db: Session = Depends(get_db)):
    return db.query(Conversation).all()

# get messages for conversation
@router.get("/messages/{conversation_id}")
def get_messages(conversation_id: int, db: Session = Depends(get_db)):
    return db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).all()

# send reply
@router.post("/reply")
def send_reply(conversation_id: int, content: str, db: Session = Depends(get_db)):
    msg = Message(
        conversation_id=conversation_id,
        sender="staff",
        content=content
    )
    db.add(msg)
    db.commit()
    return {"status": "sent"}
