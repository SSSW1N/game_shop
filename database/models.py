from sqlalchemy import String, Integer, Boolean, ForeignKey, DateTime, Column, Float
from sqlalchemy.orm import relationship

from database import Base

# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
    balance = Column(Float, default=0)


# Таблица игр
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, autoincrement=True, primary_key=True)
    game_name = Column(String)
    game_desc = Column(String)
    game_price = Column(Float, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery', foreign_keys=[user_id])

# Таблица оплаты
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    status = Column(Boolean)

    reg_date = Column(DateTime)

    game_fk = relationship(Game, lazy='subquery', foreign_keys=[game_id])
    user_fk = relationship(User, lazy='subquery', foreign_keys=[user_id])


# Таблица комментариев
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, autoincrement=True, primary_key=True)
    comment_text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))

    reg_date =Column(DateTime)

    game_fk = relationship(Game, lazy='subquery', foreign_keys=[game_id])
    user_fk = relationship(User, lazy='subquery', foreign_keys=[user_id])

class UserKorzina(Base):
    __tablename__ = 'korzina'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))


    user_fk = relationship(User, lazy='subquery', foreign_keys=[user_id])
    game_fk = relationship(Game, lazy='subquery', foreign_keys=[game_id])


