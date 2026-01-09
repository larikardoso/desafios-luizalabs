from fastapi import APIRouter
from app.atleta.controller import router as atleta
from app.categorias.controller import router as categoria
from app.centro_treinamento.controller import router as centro_treinamento


api_router = APIRouter()
api_router.include_router(atleta, prefix="/atletas", tags=["atletas"])
api_router.include_router(categoria, prefix="/categorias", tags=["categorias"])
api_router.include_router(centro_treinamento, prefix="/centros_treinamentos", tags=["centros_treinamentos"])