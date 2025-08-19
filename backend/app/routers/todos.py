from datetime import datetime, timezone
from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query, Depends
from pydantic import BaseModel, Field
from starlette import status
from utils.dynamodb import get_todos_table
from boto3.dynamodb.conditions import Key
from controllers import todoController
from services.authService import get_current_user

router = APIRouter(
    prefix='/todos',
    tags=['todos']
)

class Todo:
    username: str #Partition key
    title: str
    description: str
    priority: int
    completed: bool
    created_at: str #Sort key
    id: str

    def __init__(self, username, title, description, priority, completed, id):
        self.username = username
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.id = id

class CreateTodoRequest(BaseModel):
    username: str = Field(description="Username of creator of the todo", default=None)
    title: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1)
    priority: int = Field(ge=1, le=3)
    completed: bool = Field(default=False)
    id: str = Field(min_length=3)

class UpdateTodoRequest(BaseModel):
    username: str
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None
    created_at: str
    id: str = Field(min_length=3)


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def read_all_todos(username: str, table=Depends(get_todos_table), current_user=Depends(get_current_user)):
    if current_user['username'] != username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    return todoController.read_all_todos(username, table)

@router.post("/create-todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo_request: CreateTodoRequest, table=Depends(get_todos_table), current_user=Depends(get_current_user)):
    if current_user['username'] != todo_request.username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    try:
        response = todoController.create_todo(todo_request, table)
        return response
    except todoController.FailedTodoCreation:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Failed to create todo.')
    
@router.put("/update-todo", status_code=status.HTTP_200_OK)
async def update_todo(todo_request: UpdateTodoRequest, table=Depends(get_todos_table), current_user=Depends(get_current_user)):
    if current_user['username'] != todo_request.username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    try:
        response = todoController.update_todo(todo_request, table)
        return response["Attributes"]
    except todoController.EmptyUpdateRequest:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nothing to update")

    
@router.delete("/{username}/{created_at}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(username: str, created_at: str, table=Depends(get_todos_table), current_user=Depends(get_current_user)):
    if current_user['username'] != username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not allowed')
    try:
        todoController.delete_todo(username, created_at, table)
    except todoController.FailedDelete:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)