from database import get_db

from datetime import datetime
from database.models import Comment

# Оставить коммент к игре
def add_comment_db(user_id, comment_text, game_id):
    db = next(get_db())

    new_comment = Comment(game_id=game_id, comment_text=comment_text, user_id=user_id)
    db.add(new_comment)
    db.commit()

    return 'Комментарий оставлен'

# Удалить коммент
def delete_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Успешно удален'

    return False

# Изменить коммент
def change_comment_db(comment_id, new_text):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        exact_comment.comment_text = new_text
        db.commit()

        return 'Коммент изменен'

    return False

# Получить все комментарии к игре
def get_all_game_comments_db(game_id):
    db = next(get_db())

    all_comments = db.query(Comment).filter_by(game_id=game_id).all()

    return all_comments

