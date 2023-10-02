from pydantic import BaseModel

class CommentModel(BaseModel):
    comment_text: str
    user_id: int
    game_id: int

class ChangeCommentModel(BaseModel):
    new_text: str
    comment_id: int