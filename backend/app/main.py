from typing import Optional
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from starlette import status
from routers import todos, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(todos.router)
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)