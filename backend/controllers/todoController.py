from datetime import datetime, timezone
from services import todoService

class EmptyUpdateRequest:
    pass

def delete_todo(username: str, created_at: str, todos_table):
    todoService.delete_todo(username, created_at, todos_table)

def read_all_todos(username: str, todos_table):
    return todoService.read_all_todos(username, todos_table)

def create_todo(todo_request, todos_table):
    todo = todo_request.model_dump()
    return todoService.create_todo(todo, todos_table)

def update_todo(todo_request, todos_table):
    updated_todo = todoService.update_todo(todo_request, todos_table)
    if not updated_todo:
        raise EmptyUpdateRequest()
    return updated_todo