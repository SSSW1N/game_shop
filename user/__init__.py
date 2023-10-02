from pydantic import BaseModel


class RegisterUserModel(BaseModel):
    name: str
    email: str
    password: str
