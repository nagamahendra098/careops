from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# ---------------- WORKSPACE ----------------
class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    timezone = Column(String)
    address = Column(String)

    users = relationship("User", back_populates="workspace")


# ---------------- USERS ----------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)  # admin or staff
    workspace_id = Column(Integer, ForeignKey("workspaces.id"))

    workspace = relationship("Workspace", back_populates="users")


# ---------------- CONTACTS ----------------
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


# ---------------- BOOKINGS ----------------
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    date = Column(String)
    time = Column(String)
    status = Column(String, default="scheduled")

    contact = relationship("Contact")


# ---------------- CONVERSATIONS ----------------
class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"))

    contact = relationship("Contact")


# ---------------- MESSAGES ----------------
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    sender = Column(String)  # system, staff, customer
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)


# ---------------- INVENTORY ----------------
class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(Integer)
    threshold = Column(Integer)


# ---------------- FORMS ----------------
class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    completed = Column(Boolean, default=False)
