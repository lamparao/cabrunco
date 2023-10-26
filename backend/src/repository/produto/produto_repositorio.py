from src.schemas.produtos.produto_schema import Produto
from sqlalchemy.orm import Session
from src.models.produtos.produto_model import Produto as produto_model

class ProdutoRepositorio:

    def __init__(self, produto: Produto, db: Session):
        self.produto = produto
        self.db = db

    async def criar_produto_respositorio(self):
        query = produto_model(**(self.produto.model_dump()))
        try:
            self.db.add(query)
            self.db.commit()
            self.db.refresh(query)
            return query
        except Exception as e:
            print(e)
        return query

