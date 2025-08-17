from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime

dynamodb = resource('dynamodb')
todos_table = dynamodb.Table('todos')


def insert_todo(todo):
    print(f'todos_insert')
    response = todos_table.put_item(
        Item=todo
    )
    print(f'Insert response: {response}')

def query_by_todo_id(value):
    print(f'select_query')
    response = {}
    filtering_exp = Key('id').eq(value)
    response = todos_table.query(
        KeyConditionExpression=filtering_exp)
    print(f'Query response: {response}')
    print(f'Query response: {response['Items']}')
