from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from starlette import status
from utils.dynamodb import get_users_table
from controllers import authController

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
    username: str = Field(min_length=3, max_length=64, description="Enter username")
    email: EmailStr
    firstname: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    password: str = Field(min_length=6, max_length=128)
    model_config = ConfigDict(populate_by_name=True)

class UserOut(BaseModel):
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    role: str = "user"

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest, users_table=Depends(get_users_table)):
    try:
        return authController.create_user(create_user_request, users_table)
    except authController.UserAlreadyExists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user")


@router.post("/token", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), users_table=Depends(get_users_table)):
    try:
        token = authController.login(form_data.username, form_data.password, users_table)
        return TokenResponse(access_token=token)
    except authController.BadCredentials:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")