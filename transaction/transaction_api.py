from fastapi import APIRouter
from transaction import BuyGameModel

from database.transactionservice import buy_game_db, get_all_payments_db

trans_router = APIRouter(prefix='/transaction', tags=['Работа с покупками'])



# Купить игру
@trans_router.post('/buy-game')
async def buy_game(data: BuyGameModel):
    try:
        result = buy_game_db(data)

        return {'status': 1, 'data': result}
    except Exception as e:
        return {'status': 0, 'data': str(e)}


# Вывести все покупки пользователя
@trans_router.get('/all-payments')
async def get_all_payments(user_id: int):
    result = get_all_payments_db(user_id)

    return {'status': 1, 'data': result}






