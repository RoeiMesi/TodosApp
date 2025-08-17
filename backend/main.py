from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from starlette import status

app = FastAPI()

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

sample_todos = [
    Todo(1, "FirstTodo", "FirstTodoDesc", 3, True),
    Todo(2, "SecondTodo", "SecondDesc", 2, False)
]

@app.get("/")
async def read_all_todos():
    return sample_todos

@app.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(todo_id: int):
    for todo in sample_todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo ID not found')