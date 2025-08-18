from datetime import datetime, timezone
from services import todoService

class EmptyUpdateRequest(Exception):
    pass

class FailedTodoCreation(Exception):
    pass

class FailedDelete(Exception):
    pass

def delete_todo(username: str, created_at: str, todos_table):
    response = todoService.delete_todo(username, created_at, todos_table)
    if not response:
        raise FailedDelete()
    return response

def read_all_todos(username: str, todos_table):
    return todoService.read_all_todos(username, todos_table)

def create_todo(todo_request, todos_table):
    todo = todo_request.model_dump()
    response = todoService.create_todo(todo, todos_table)
    if not response:
        raise FailedTodoCreation()
    return response


def update_todo(todo_request, todos_table):
    updated_todo = todoService.update_todo(todo_request, todos_table)
    if not updated_todo:
        raise EmptyUpdateRequest()
    return updated_todo