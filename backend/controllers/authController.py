from pydantic import BaseModel
from services import authService
from fastapi.security import OAuth2PasswordBearer

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class UserAlreadyExists(Exception):
    pass

class BadCredentials(Exception):
    pass

def create_user(user_request: BaseModel, users_table):
    created = authService.create_user(
        username=user_request.username,
        email = user_request.email,
        password = user_request.password,
        firstname=user_request.firstname,
        lastname=user_request.lastname,
        users_table=users_table,
    )

    if created is None:
        raise UserAlreadyExists()
    return created

def login(username: str, password: str, users_table):
    token = authService.login_for_access_token(username=username, password=password, users_table=users_table)
    if not token:
        raise BadCredentials()
    return token