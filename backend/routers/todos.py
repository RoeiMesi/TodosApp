from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status

router = APIRouter()

class Todo:
    id: int
    title: str
    description: str
    priority: int
    completed: bool

    def __init__(self, id, title, description, priority, completed):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed

class TodoRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1)
    priority: int = Field(ge=1, le=3)
    completed: bool = Field(default=False)


TODOS = [
    Todo(1, "FirstTodo", "FirstTodoDesc", 3, True),
    Todo(2, "SecondTodo", "SecondDesc", 2, False)
]

@router.get("/")
async def read_all_todos():
    return TODOS

@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(todo_id: int):
    for todo in TODOS:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo ID not found')

@router.post("/create-todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo_request: TodoRequest):
    new_todo = Todo(**todo_request.model_dump())
    TODOS.append(find_todo_id(new_todo))

def find_todo_id(todo):
    todo.id = 1 if len(TODOS) == 0 else len(TODOS) + 1
    return todo

@router.put("/todos/update-todo", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo_request: TodoRequest):
    todo_changed = False
    for i in range(len(TODOS)):
        if TODOS[i].id == todo_request.id:
            TODOS[i] = todo_request
            todo_changed = True
    if todo_changed == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo ID not found.')
    