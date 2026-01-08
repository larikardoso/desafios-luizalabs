from fastapi import APIRouter, status, Body, HTTPException
from app.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from app.centro_treinamento.models import CentroTreinamentoModel
from uuid import uuid4
from pydantic import UUID4

from app.contrib.repository.dependencies import DatabaseDependency
from fastapi.params import Body as body

from sqlalchemy.future import select

router = APIRouter()

@router.post(
    '/', 
    summary = "Cria um novo centro de treinamento",
    status_code = status.HTTP_201_CREATED,
    response_model = CentroTreinamentoOut
)

async def post(
    db_session: DatabaseDependency, 
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_in.model_dump())
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    
    return centro_treinamento_out

@router.get(
    '/', 
    summary="Retorna todos os centros de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)

async def query(db_session: DatabaseDependency,) -> list[CentroTreinamentoOut]:
    centros_treinamento: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    
    return centros_treinamento

@router.get(
    '/{id}', 
    summary="Consulte um centro de treinamento pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)

async def query(db_session: DatabaseDependency, id: UUID4) -> CentroTreinamentoOut:
    centro_treinamento: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Centro de treinamento não encontrado no id: {id}"
        )

    return centro_treinamento