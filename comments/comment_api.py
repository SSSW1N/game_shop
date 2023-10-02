from fastapi import APIRouter

from database.commentservice import add_comment_db, delete_comment_db, change_comment_db, get_all_game_comments_db

from comments import CommentModel, ChangeCommentModel

comment_router = APIRouter(prefix='/comments', tags=['Работа с комментариями'])

# Оставить коммент
@comment_router.post('/add-comment')
async def add_comment(data: CommentModel):
    result = add_comment_db(**data.model_dump())

    return {'status': 1, 'data': result}



# Удалить коммент
@comment_router.delete('/delete-comment')
async def delete_comment(comment_id: str):
    result = delete_comment_db(comment_id)

    if result:
        return {'status': 1, 'data': result}

    return {'status': 0, 'data': 'Комментарий не найден'}

# Изменить коммент
@comment_router.put('/change-comment')
async def change_comment(data: ChangeCommentModel):
    result = change_comment_db(**data.model_dump())

    if result:
        return {'status': 1, 'data': result}

    return {'status': 0, 'data': 'Комментарий не найден'}

# Получить все комментарии к игре
@comment_router.get('/get-all-comments')
async def get_comments(game_id: int):
    result = get_all_game_comments_db(game_id)

    return {'status': 1, 'data': result}








