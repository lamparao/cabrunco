from src.core.database import Base
from sqlalchemy import Column, Integer, String, BigInteger, DECIMAL, DATETIME
from decimal import Decimal
from datetime import datetime

class Produto(Base):
    __tablename__ = "produto"

    id_produto: int = Column(Integer, primary_key=True, index=True)
    nome_produto: str = Column(String(255))
    codigo_barra: int = Column(BigInteger, unique=True)
    gtin: str = Column(String, nullable=True)
    data_criacao: datetime = Column(DATETIME, default=datetime.now())
    data_update: datetime = Column(DATETIME, nullable=True)
    data_deleted: datetime = Column(DATETIME, nullable=True)