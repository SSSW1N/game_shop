from sqlalchemy import String, Integer, Boolean, ForeignKey, DateTime, Column, Float
from sqlalchemy.orm import relationship

from database import Base

# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)

    reg_date = Column(DateTime)

# Таблица игр
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, autoincrement=True, primary_key=True)
    game_name = Column(String)
    game_desc = Column(String)
    game_photo = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery', foreign_keys=[user_id])

class UploadPhoto(Base):
    __tablename__ = 'uploads'
    id = Column(Integer, autoincrement=True, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    game_photo = Column(String)

    game_fk = relationship(Game, lazy='subquery')

class UserCart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))


    user_fk = relationship(User, lazy='subquery', foreign_keys=[user_id])
    game_fk = relationship(Game, lazy='subquery', foreign_keys=[game_id])


# Таблица комментариев
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, autoincrement=True, primary_key=True)
    comment_text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    rating = Column(Float, default=0)

    reg_date =Column(DateTime)

    game_fk = relationship(Game, lazy='subquery', foreign_keys=[game_id])
    user_fk = relationship(User, lazy='subquery', foreign_keys=[user_id])



