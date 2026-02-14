from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.models import Workspace

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/workspace")
def create_workspace(name: str, email: str, timezone: str, address: str, db: Session = Depends(get_db)):
    ws = Workspace(
        name=name,
        email=email,
        timezone=timezone,
        address=address
    )
    db.add(ws)
    db.commit()
    db.refresh(ws)
    return ws
