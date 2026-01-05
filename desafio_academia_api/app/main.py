from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import alunos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Academia API")

app.include_router(alunos.router)
