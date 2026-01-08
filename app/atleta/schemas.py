from typing import Annotated, Optional
from pydantic import BaseModel, Field, PositiveFloat

from app.categorias.schemas import CategoriaIn
from app.centro_treinamento.schemas import CentroTreinamentoAtleta
from app.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", max_length=100, example="João Silva")]
    cpf: Annotated[str, Field(description="CPF do atleta", min_length=11, max_length=11, example="12345678901")]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta em kg", example=70.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta em metros", example=1.75)]
    sexo: Annotated[str, Field(description="Sexo do atleta", max_length=1, example="M")]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")]
    
class AtletaIn(Atleta):
    pass
    
class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="Nome do atleta", max_length=100, example="João Silva")]
    idade: Annotated[Optional[int], Field(None, description="Idade do atleta", example=25)]
    
class AtletaListOut(BaseModel):
    nome: str
    categoria: str
    centro_treinamento: str

    class Config:
        from_attributes = True