from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, HTTPException, Query, status, Body
from fastapi_pagination import LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate
from pydantic import UUID4
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from app.atleta.models import AtletaModel
from app.atleta.schemas import AtletaIn, AtletaListOut, AtletaOut, AtletaUpdate

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
    
    atleta = AtletaModel(**atleta_in.model_dump(
        exclude={'categoria', 'centro_treinamento'}), 
        categoria_id=categoria.pk_id, 
        centro_treinamento_id=centro_treinamento.pk_id)

    try:
        db_session.add(atleta)
        await db_session.commit()
        await db_session.refresh(atleta)
    
    except IntegrityError:
        await db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Atleta com CPF '{atleta_in.cpf}' já existe."
        )

    return AtletaOut.model_validate(atleta)


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
    '/',
    summary="Lista atletas",
    response_model=LimitOffsetPage[AtletaListOut],
    status_code=200
)
async def query(
    db_session: DatabaseDependency,
    nome: str | None = Query(None),
    cpf: str | None = Query(None),
):
    query = (
        select(AtletaModel)
        .options(
            selectinload(AtletaModel.categoria),
            selectinload(AtletaModel.centro_treinamento)
        )
    )

    if nome:
        query = query.filter(AtletaModel.nome.ilike(f"%{nome}%"))

    if cpf:
        query = query.filter(AtletaModel.cpf == cpf)

    return await paginate(
        db_session,
        query,
        transformer=lambda atletas: [
            AtletaListOut(
                nome=a.nome,
                categoria=a.categoria.nome,
                centro_treinamento=a.centro_treinamento.nome
            )
            for a in atletas
        ]
    )


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