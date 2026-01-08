from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4
from sqlalchemy.future import select
from app.atleta.models import AtletaModel
from app.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate

from app.categorias.models import CategoriaModel
from app.centro_treinamento.models import CentroTreinamentoModel
from app.contrib.repository.dependencies import DatabaseDependency
from fastapi.params import Body as body

router = APIRouter()

@router.post(
    '/', 
    summary = "Cria um novo atleta",
    status_code = status.HTTP_201_CREATED,
    response_model=AtletaOut
)

async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome
    
    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_nome))
    ).scalars().first()
    
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Categoria '{categoria_nome}' não encontrada."
        )

    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome))
    ).scalars().first()

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Centro de treinamento '{centro_treinamento_nome}' não encontrado."
        )

    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        
        atleta_model = AtletaModel(**atleta_in.model_dump(exclude={'categoria', 'centro_treinamento'}), categoria_id=categoria.pk_id, centro_treinamento_id=centro_treinamento.pk_id)
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar atleta"
        )

    return atleta_out

@router.get(
    '/', 
    summary="Retorna todas os atletas",
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)

async def query(db_session: DatabaseDependency,) -> list[AtletaOut]:
    atletas: list[AtletaOut] = (await db_session.execute(select(AtletaModel))).scalars().all()
    
    return [AtletaOut.model_validate(atleta) for atleta in atletas]

@router.get(
    '/{id}', 
    summary="Consulte um atleta pelo id",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)

async def query(db_session: DatabaseDependency, id: UUID4) -> AtletaOut:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id: {id}"
        )

    return atleta

@router.patch(
    '/{id}', 
    summary="Editar um atleta pelo id",
    status_code=status.HTTP_200_OK, 
    response_model=AtletaOut,
)

async def get(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id: {id}"
        )
        
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_update.items():
        setattr(atleta, key, value)
    
    await db_session.commit()
    await db_session.refresh(atleta)
    
    return atleta

@router.delete(
    '/{id}', 
    summary="Deleta um atleta pelo id",
    status_code=status.HTTP_204_NO_CONTENT,
    
)
async def get(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id: {id}"
        )

    await db_session.delete(atleta)
    await db_session.commit()