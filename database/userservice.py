from datetime import datetime


from database import get_db
from database.models import User, UserKorzina


# Регистрация пользователя
def register_user_db(name, surname, email, phone_number, password):
    db = next(get_db())

    cheker = db.query(User).filter_by(email=email).first()

    if cheker:
        return False

    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number,
                    password=password)

    db.add(new_user)
    db.commit()

    return 'Пользователь успешно зарегистрирован'

# Проверка на наличие пользователя
def check_user_db(phone_number: int, password: str = None):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number, password=password).first()

    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Неверный пароль'
    return False


# Корзина пользователя
def get_all_user_games_db(user_id):
    db = next(get_db())

    user_games = db.query(UserKorzina).filter_by(user_id=user_id).all()

    return user_games

# Добавление в корзину
def add_game_db(game_id, user_id):
    db = next(get_db())

    new_game = UserKorzina(user_id=user_id, id=game_id)

    db.add(new_game)
    db.commit()

    return 'Успешно добавлено'


# Удаление из корзины
def delete_game_db(game_id):
    db = next(get_db())

    exact_game = db.query(UserKorzina).filter_by(id=game_id).first()


    db.delete(exact_game)
    db.commit()

    return 'Успешно удалено'


# Пополнить баланс
def replenishment_balance_db(user_id, balance):
    db = next(get_db())

    # тут должно быть апи банка

    cheker = db.query(User).filter_by(id=user_id).first()

    if cheker:
        rep_balance = User(balance=balance, id=user_id)

        db.add(rep_balance)

        db.commit()






