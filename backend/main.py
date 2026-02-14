from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.workspace import router as workspace_router
from routes.contact import router as contact_router
from routes.booking import router as booking_router
from routes.inbox import router as inbox_router
from routes.dashboard import router as dashboard_router
from routes.calendar import router as calendar_router
from routes.public import router as public_router










app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://careops-mauve.vercel.app",   # your frontend
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(workspace_router)
app.include_router(contact_router)
app.include_router(booking_router)
app.include_router(inbox_router)
app.include_router(dashboard_router)
app.include_router(calendar_router)
app.include_router(public_router)



