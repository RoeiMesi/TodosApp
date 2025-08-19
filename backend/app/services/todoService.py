from datetime import datetime, timezone
from boto3.dynamodb.conditions import Key

def delete_todo(username: str, created_at: str, todos_table):
    try:
        todos_table.delete_item(
        Key={"username": username, "created_at": created_at},
        ConditionExpression="attribute_exists(username) AND attribute_exists(created_at)"
        )
        return True
    except:
        return None


def read_all_todos(username: str, todos_table):
    filtering_exp = Key('username').eq(username)
    response = todos_table.query(
        KeyConditionExpression=filtering_exp)
    return response.get("Items", [])

def create_todo(todo, todos_table):
    try:
        todo['created_at'] = datetime.now(timezone.utc).isoformat()
        todos_table.put_item(Item = todo)
        return todo
    except:
        return None

def update_todo(todo_request, todos_table):
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
        return None

    update_expression = "SET " + ", ".join(f"#{key} = :{key}" for key in to_set)
    expression_attr_names = {f"#{key}": key for key in to_set}
    expression_attr_vals = {f":{key}": val for key, val in to_set.items()}

    response = todos_table.update_item(
        Key={
            "username": todo_request.username,
            "created_at": todo_request.created_at
            },
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attr_names,
        ExpressionAttributeValues=expression_attr_vals,
        ConditionExpression="attribute_exists(username) AND attribute_exists(created_at)",
        ReturnValues="ALL_NEW",
    )
    return response