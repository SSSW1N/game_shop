from fastapi import APIRouter, Body

from games import ChangeGameDescModel
from database.gamesservice import add_game_db, delete_game_db, change_game_info_db, get_all_games_db, get_exact_game_db



game_router = APIRouter(prefix='/game', tags=['Управление играми'])

# Добавить игру
@game_router.post('/add-game')
async def add_game(user_id: int = Body(...), game_name: str = Body(...), game_desc: str = Body(...),
                   game_price: float = Body(...)):
    try:
        result = add_game_db(user_id, game_name, game_desc, game_price)

        return {'status': 1, 'data': result}

    except Exception as e:
        return {'status': 0, 'data': str(e)}

# Удалить игру
@game_router.delete('/delete-game')
async def delete_game(user_id: int, game_id: int):
    result = delete_game_db(user_id, game_id)

    if result:
        return {'status': 1, 'data': result}

    return {"status": 0, 'data': 'Пост не найден'}


# Изменить описание игры
@game_router.put('/change-game-desc')
async def change_game_decs(data: ChangeGameDescModel):
    result = change_game_info_db(**data.model_dump())

    if result:
        return {'status': 1, 'data': result}

    return {'status': 0, 'data': 'Не найдено'}


# Показать все игры
@game_router.get('/get-all-games')
async def get_all_games():
    result = get_all_games_db()

    return {'status': 1, 'data': result}

# Найти игру по названию
@game_router.get('/get-exact-game')
async def get_exact_game(game_id: int, game_name: str = None):
    result = get_exact_game_db(game_id, game_name)

    if result:
        return {'status': 1, 'data': result}

    return {'status': 0, 'data': 'Не найдено'}






