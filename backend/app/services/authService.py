from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from settings import settings
from starlette import status
from fastapi.security import OAuth2PasswordBearer
from utils.dynamodb import get_users_table

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def create_user(username: str, email: str, firstname: str, lastname: str, password: str, users_table):
    existing = users_table.get_item(Key={"username": username})
    if "Item" in existing:
        return None # The username already exists.
    
    hashed_password = bcrypt_context.hash(password)
    item = {
        "username": username,
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "hashed_password": hashed_password,
        "role": "user",
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    users_table.put_item(Item = item)
    return {
        "username": item["username"],
        "email": item["email"],
        "firstname": item["firstname"],
        "lastname": item["lastname"],
        "role": "user",
    }

def authenticate_user(username, password, users_table):
    existing = users_table.get_item(Key = {'username': username})
    if "Item" not in existing:
        return None
    user = existing['Item']
    hashed_password = user['hashed_password']
    if bcrypt_context.verify(password, hashed_password):
        return user
    return None

def create_access_token(username: str, email: str, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'email': email, 'role': role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def login_for_access_token(username, password, users_table):
    user = authenticate_user(username, password, users_table)
    if not user:
        return None
    token = create_access_token(username=user['username'], email=user['email'], role=user['role'], expires_delta=timedelta(minutes=60))
    return token

def get_current_user(users_table=Depends(get_users_table), token: str = Depends(oauth2_bearer)):
    data = decode_token(token)
    if not data or "sub" not in data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    username = data['sub']
    resp = users_table.get_item(Key={'username': username})
    user = resp.get('Item')
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    return user


def decode_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None