from fastapi import FastAPI

from user.user_api import user_router
from games.games_api import game_router
from comments.comment_api import comment_router



# Для запуска БД
from database import Base, engine
Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(game_router)
app.include_router(comment_router)





