from typing import Annotated
from pydantic import UUID4, Field

from app.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", max_length=20, example="CT King")]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", max_length=60, example="Rua das Flores, 123")]
    proprietario: Annotated[str, Field(description="Nome do proprietário do centro de treinamento", max_length=30, example="Carlos Silva")]
    
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", max_length=20, example="CT King")]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador único do centro de treinamento")]