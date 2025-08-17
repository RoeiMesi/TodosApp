from datetime import datetime, timezone
from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query, Depends
from pydantic import BaseModel, Field
from starlette import status
from utils.dynamodb import get_todos_table
from boto3.dynamodb.conditions import Key

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

    def __init__(self, username, title, description, priority, completed):
        self.username = username
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.created_at = datetime.now(timezone.utc).isoformat()

class CreateTodoRequest(BaseModel):
    username: str = Field(description="Username of creator of the todo", default=None)
    title: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1)
    priority: int = Field(ge=1, le=3)
    completed: bool = Field(default=False)

class UpdateTodoRequest(BaseModel):
    username: str
    created_at: str
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def read_todos(username: str, table=Depends(get_todos_table)):
    filtering_exp = Key('username').eq(username)
    response = table.query(
        KeyConditionExpression=filtering_exp)
    if not response["Items"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No todos found')
    return response["Items"]

@router.post("/create-todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo_request: CreateTodoRequest, table=Depends(get_todos_table)):
    todo_request_model = todo_request.model_dump()
    todo_request_model['created_at'] = datetime.now(timezone.utc).isoformat()
    response = table.put_item(Item = todo_request_model)
    print("Todo created successfully")


@router.put("/update-todo", status_code=status.HTTP_200_OK)
async def update_todo(todo_request: UpdateTodoRequest, table=Depends(get_todos_table)):
    title_val = "" if todo_request.title is None else todo_request.title
    description_val = "" if todo_request.description is None else todo_request.description
    priority_val = 0 if todo_request.priority is None else todo_request.priority

    response = table.update_item(
        Key={
            "username": todo_request.username,
            "created_at": todo_request.created_at
            },
        UpdateExpression="SET title = :title, description = :desc, priority = :priority",
        ExpressionAttributeValues={
            ":title": title_val,
            ":desc": description_val,
            ":priority": priority_val,
        },
        ReturnValues="ALL_NEW",
    )

    if "Attributes" not in response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    return response["Attributes"]
    