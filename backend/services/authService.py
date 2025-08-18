from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = '0f2963b4573016418f474d9398ed6776afa7e2c0baa1b9edefd711c99f0e8ca9'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

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
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def login_for_access_token(username, password, users_table):
    user = authenticate_user(username, password, users_table)
    if not user:
        return None
    token = create_access_token(username=user['username'], email=user['email'], role=user['role'], expires_delta=timedelta(minutes=60))
    return token
        