from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import LimitOffsetPage, Params
from fastapi_pagination.ext.sqlalchemy import paginate

from ..database import get_db
from ..models import Aluno
from ..schemas import AlunoCreate, AlunoOut

router = APIRouter(prefix="/alunos", tags=["aluno"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=AlunoOut
)
def registrar_aluno(
    payload: AlunoCreate,
    db: Session = Depends(get_db)
):
    aluno = Aluno(**payload.model_dump())
    try:
        db.add(aluno)
        db.commit()
        db.refresh(aluno)
        return aluno
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="CPF já cadastrado",
        )


@router.get("/", response_model=LimitOffsetPage[AlunoOut])
def listar_alunos(
    nome: str | None = None,
    cpf: str | None = None,
    params: Params = Depends(),
    db: Session = Depends(get_db),
):
    query = db.query(Aluno)

    if nome:
        query = query.filter(Aluno.nome.ilike(f"%{nome}%"))

    if cpf:
        query = query.filter(Aluno.cpf == cpf)

    return paginate(db, query)