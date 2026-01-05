from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Treino(Base):
    __tablename__ = "treinos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
