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
    created_at: str
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None
    id: str = Field(min_length=3)


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def read_todos(username: str, table=Depends(get_todos_table)):
    filtering_exp = Key('username').eq(username)
    response = table.query(
        KeyConditionExpression=filtering_exp)
    return response["Items", []]

@router.post("/create-todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo_request: CreateTodoRequest, table=Depends(get_todos_table)):
    item = todo_request.model_dump()
    item['created_at'] = datetime.now(timezone.utc).isoformat()
    table.put_item(Item = item)
    return item
    

@router.put("/update-todo", status_code=status.HTTP_200_OK)
async def update_todo(todo_request: UpdateTodoRequest, table=Depends(get_todos_table)):
    to_set = {}
    if todo_request.title is not None:
        to_set['title'] = todo_request.title
    if todo_request.description is not None:
        to_set['description'] = todo_request.description
    if todo_request.priority is not None:
        to_set['priority'] = todo_request.priority
    if todo_request.completed is not None:
        to_set['completed'] = todo_request.completed

    if not to_set:
        return {"message": "Nothing to update"}

    update_expression = "SET " + ", ".join(f"#{key} = :{key}" for key in to_set)
    expression_attr_names = {f"#{key}": key for key in to_set}
    expression_attr_vals = {f":{key}": val for key, val in to_set.items()}

    response = table.update_item(
        Key={
            "username": todo_request.username,
            "created_at": todo_request.created_at
            },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attr_names,
        ExpressionAttributeValues=expression_attr_vals,
        ConditionExpression="attribute_exists(username) AND attribute_exists(created_at)",
        ReturnValues="ALL_NEW",
    )
    return response["Attributes"]
    
@router.delete("/{username}/{created_at}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(username: str, created_at: str, table=Depends(get_todos_table)):
    table.delete_item(
        Key={"username": username, "created_at": created_at},
        ConditionExpression="attribute_exists(username) AND attribute exists(created_at)"
    )