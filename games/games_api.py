from fastapi import APIRouter, Body, UploadFile

from games import ChangeGameDescModel, RegisterGameModel
from database.gamesservice import add_game_db, upload_photo_db,  delete_game_db, change_game_info_db,\
    get_all_games_db, get_exact_game_db



game_router = APIRouter(prefix='/game', tags=['Управление играми'])

# Добавить игру на сайт
@game_router.post('/add-game')
async def add_game(data: RegisterGameModel):
    result = add_game_db(**data.model_dump())

    return {'status': 1, 'data': result}

# Удалить игру с сайта
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

# Найти игру
@game_router.get('/get-exact-game')
async def get_exact_game(game_id: int):
    result = get_exact_game_db(game_id)

    if result:
        return {'status': 1, 'data': result}

    return {'status': 0, 'data': 'Не найдено'}

@game_router.post('/upload-photo')
async def upload_photo(game_id: int = Body(...),
                                user_id: int = Body(...),
                                game_photo: UploadFile = None):
    photo_path = f'./media/{game_photo.filename}'

    try:
        with open(f'./media/{game_photo.filename}', 'wb') as file:
            user_photo = await game_photo.read()

            file.write(user_photo)

        result = upload_photo_db(game_id=game_id, game_photo=photo_path)

    except Exception as e:
        result = e

    return {'status': 1, 'data': result}










