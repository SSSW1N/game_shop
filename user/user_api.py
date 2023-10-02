from fastapi import APIRouter, Body
from user import RegisterUserModel
from database.userservice import replenishment_balance_db, register_user_db, get_all_user_games_db, check_user_db, add_game_db, delete_game_db


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
async def login_user(phone_number: int = Body(...), password: str = Body(...)):
    result = check_user_db(phone_number, password)

    return {'status': 1, 'data': result}

# Библиотека пользователя
@user_router.get('/list-of-games')
async def get_all_user_games(user_id: int):
    result = get_all_user_games_db(user_id)

    return {'status': 1, 'data': result}

# Добавление в корзину
@user_router.get('/add-game-in-korzinu')
async def add_game_in_korzina(game_id: int, user_id: int):
    try:
        result = add_game_db(user_id, game_id)

        return {'status': 1, 'data': result}

    except Exception as e:
        return {'status': 0, 'data': str(e)}

# Удаление из корзины
@user_router.delete('/delete-game-from-korzina')
async def delete_game_from_korzina(game_id: int):
    result = delete_game_db(game_id)

    return {'status': 1, 'data': result}

# Пополнение баланса
@user_router.post('/popolnenie')
async def replenishment_balance(user_id: int, balance: float):
    result = replenishment_balance_db(user_id, balance)

    return {'status': 1, 'data': result}


