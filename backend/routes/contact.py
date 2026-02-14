from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Contact, Conversation, Message

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/contact")
def create_contact(name: str, email: str = None, phone: str = None, db: Session = Depends(get_db)):

    # create contact
    contact = Contact(name=name, email=email, phone=phone)
    db.add(contact)
    db.commit()
    db.refresh(contact)

    # create conversation
    convo = Conversation(contact_id=contact.id)
    db.add(convo)
    db.commit()
    db.refresh(convo)

    # send welcome message
    msg = Message(
        conversation_id=convo.id,
        sender="system",
        content="Welcome! Thanks for contacting us."
    )
    db.add(msg)
    db.commit()

    return {
        "contact_id": contact.id,
        "conversation_id": convo.id
    }
