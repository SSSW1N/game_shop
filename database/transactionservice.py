from database.models import Transaction, Game, User
from datetime import datetime

from database import get_db

from transaction import BuyGameModel

# Покупка игры
def buy_game_db(data: BuyGameModel):
    db = next(get_db())

    user_balance = db.query(User).filter_by(balance=data.balance, id=data.user_id).first()
    price_of_game = db.query(Game).filter_by(game_price=data.game_price, id=data.game_id).first()

    if user_balance.balance >= data.game_price:
        user_balance.balance -= price_of_game.game_price

        transaction = data.model_dump()
        new_transaction = Transaction(reg_date=datetime.now(), **transaction)

        db.add(new_transaction)
        db.commit()
        return True
    return False

# Вывести все покупки пользователя
def get_all_payments_db(user_id: int):
    db = next(get_db())

    payments = db.query(Transaction).filter_by(user_id=user_id).all()

    return payments


