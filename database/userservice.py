from datetime import datetime


from database import get_db
from database.models import User, UserCart


# Регистрация пользователя
def register_user_db(name, email, password):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return False

    new_user = User(name=name, email=email, password=password, reg_date=datetime.now())

    db.add(new_user)
    db.commit()

    return 'Пользователь успешно зарегистрирован'

# Проверка на наличие пользователя
def check_user_db(email: str, password: str = None):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email, password=password).first()

    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Неверный пароль'
    return False

# Добавление в корзину
def add_game_in_cart_db(game_id, user_id):
    db = next(get_db())

    new_game = UserCart(game_id=game_id, user_id=user_id)

    db.add(new_game)
    db.commit()

    return 'Успешно добавлено'


# Удаление из корзины
def delete_game_db(game_id, user_id):
    db = next(get_db())

    exact_game = db.query(UserCart).filter_by(user_id=user_id, game_id=game_id).first()

    if exact_game:
        db.delete(exact_game)
        db.commit()

        return 'Успешно удалено'

    return False

# Корзина пользователя
def get_all_user_games_db(user_id):
    db = next(get_db())

    user_games_cart = db.query(UserCart).filter_by(user_id=user_id).all()
    if user_games_cart:
        return user_games_cart
    return False







