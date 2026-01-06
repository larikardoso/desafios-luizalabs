from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.database import Base, engine
from app.routers import alunos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Academia API")

app.include_router(alunos.router)
add_pagination(app)


@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à Academia API!"}