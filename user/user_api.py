from fastapi import APIRouter, Body
from user import RegisterUserModel
from database.userservice import register_user_db, get_all_user_games_db, check_user_db, add_game_in_cart_db, delete_game_db


user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])


# Регистрация пользователя
@user_router.post('/register')
async def register_user(data: RegisterUserModel):
    result = register_user_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пользователь с такой почтой уже есть'}


# Вход пользователя
@user_router.post('/login')
async def login_user(email: str = Body(...), password: str = Body(...)):
    result = check_user_db(email, password)

    return {'status': 1, 'data': result}


# Добавление в корзину
@user_router.post('/add-game-in-cart')
async def add_game_in_cart(game_id: int, user_id: int):
    result = add_game_in_cart_db(game_id, user_id)

    return {'status': 1, 'data': result}


# Удаление из корзины
@user_router.delete('/delete-game-from-cart')
async def delete_game_from_cart(game_id: int, user_id: int):
    result = delete_game_db(game_id, user_id)
    if result:
        return {'status': 1, 'data': result}
    return {'status': 0, 'data': 'Не найдено'}


# Библиотека пользователя
@user_router.get('/list-of-games')
async def get_all_user_games(user_id: int):
    result = get_all_user_games_db(user_id)

    return {'status': 1, 'data': result}

