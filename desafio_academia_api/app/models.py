from sqlalchemy import Column, Integer, String
from .database import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=True)
    cpf = Column(String(11), nullable=False, unique=True)
    centro_treinamento = Column(String(100))
    categoria = Column(String(50))