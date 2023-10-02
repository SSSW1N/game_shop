from pydantic import BaseModel


class RegisterGameModel(BaseModel):
    game_name: str
    game_desc: str
    user_id: int

class ChangeGameDescModel(BaseModel):
    game_id: int
    new_desc: str
    user_id: int



