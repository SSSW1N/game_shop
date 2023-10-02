from datetime import datetime

from database.models import Game, UploadPhoto
from database import get_db

# Добавить игру
def add_game_db(user_id: int, game_name: str , game_desc: str):
    db = next(get_db())

    new_game = Game(game_name=game_name, game_desc=game_desc, user_id=user_id, reg_date=datetime.now())

    db.add(new_game)
    db.commit()

    return 'Игра успешна добавлена'

# Добавить фото к игре
def upload_photo_db(game_id, game_photo):
    db = next(get_db())

    new_game_photo = UploadPhoto(game_id=game_id, game_photo=game_photo)

    if new_game_photo:
        db.add(new_game_photo)
        db.commit()

        return 'Успешно загружено'
    return False


# Удалить игру
def delete_game_db(user_id: int, game_id: int):
    db = next(get_db())

    exact_game = db.query(Game).filter_by(id=game_id, user_id=user_id).first()

    if exact_game:
        db.delete(exact_game)
        db.commit()

        return 'Игра успешно удалена'

    return False


# Изменить описание игры
def change_game_info_db(user_id, game_id, new_desc):
    db = next(get_db())

    checker = db.query(Game).filter_by(id=game_id, user_id=user_id).first()

    if checker:
        checker.game_desc = new_desc
        db.commit()

        return 'успешно изменен'

    return False

# Показать все игры
def get_all_games_db():
    db = next(get_db())

    all_games = db.query(Game).all()

    return all_games


# Найти игру
def get_exact_game_db(game_id: int):
    db = next(get_db())

    exact_game = db.query(Game).filter_by(id=game_id).first()
    if exact_game:
        return exact_game

    return False

















