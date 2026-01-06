from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    cpf: str
    idade: int | None = None
    centro_treinamento: str | None = None

class AlunoCreate(AlunoBase):
    pass

class AlunoOut(BaseModel):
    nome: str
    idade: int | None = None
    centro_treinamento: str | None = None
    categoria: str | None = None

    model_config = {
        "from_attributes": True
    }