from typing import Optional
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from starlette import status
from routers import todos

app = FastAPI()

app.include_router(todos.router)