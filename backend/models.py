from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    telefone: str
    ordens: List["OrdemServico"] = Relationship(back_populates="cliente")

class Tecnico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    especialidade: str
    ordens: List["OrdemServico"] = Relationship(back_populates="tecnico")

class OrdemServico(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    descricao: str
    status: str = Field(default="Aberta") # Aberta, Em Andamento, Concluída
    
    cliente_id: Optional[int] = Field(default=None, foreign_key="cliente.id")
    cliente: Optional[Cliente] = Relationship(back_populates="ordens")
    
    tecnico_id: Optional[int] = Field(default=None, foreign_key="tecnico.id")
    tecnico: Optional[Tecnico] = Relationship(back_populates="ordens")