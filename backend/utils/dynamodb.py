from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime

dynamodb = resource('dynamodb')
users_table = dynamodb.Table('users')
todos_table = dynamodb.Table('todos')

def get_users_table():
    return users_table

def get_todos_table():
    return todos_table