from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from starlette import status
from utils.dynamodb import get_users_table

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

class User:
    username: str #Partition key
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

class CreateUserRequest(BaseModel):
    username: str = Field(description="Enter username")
    email: str
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    password: str = Field(min_length=1)
    role: str


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest, table=Depends(get_users_table)):
    response = table.put_item(Item = create_user_request.model_dump())
    print('Successfully created user!')
