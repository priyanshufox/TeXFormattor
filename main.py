from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# Update CORS settings for production
origins = [
    "http://localhost:3000",  # Your local frontend
    "https://your-frontend-domain.com"  # Replace with your frontend domain when deployed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ... rest of your existing code ... 