from pydantic import BaseModel
from decimal import Decimal

class Produto(BaseModel):
    pass

class ProdutoIn(Produto):
    nome_produto: str
    codigo_barra: int
    gtin: str