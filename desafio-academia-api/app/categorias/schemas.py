from typing import Annotated

from pydantic import Field, UUID4
from app.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", max_length=10, example="Leve")]
    
class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador único da categoria")]