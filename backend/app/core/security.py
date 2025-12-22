import bcrypt
import hashlib


def hash_password(password: str) -> str:
    password = password.encode("utf-8")[:72]
    return bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    password = password.encode("utf-8")[:72]
    return bcrypt.checkpw(password, hashed.encode("utf-8"))


def hash_long_secret(secret: str) -> str:
    """
    Для длинных секретов (ФНС, токены и т.п.)
    """
    sha = hashlib.sha256(secret.encode("utf-8")).digest()
    return bcrypt.hashpw(sha, bcrypt.gensalt()).decode("utf-8")


def verify_long_secret(secret: str, hashed: str) -> bool:
    sha = hashlib.sha256(secret.encode("utf-8")).digest()
    return bcrypt.checkpw(sha, hashed.encode("utf-8"))
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(user_id: int, role: str) -> str:
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
