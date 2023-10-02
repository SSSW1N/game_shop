from pydantic import BaseModel


class RegisterUserModel(BaseModel):
    name: str
    surname: str
    phone_number: int
    email: str
    password: str
