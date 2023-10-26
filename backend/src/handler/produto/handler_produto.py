from src.schemas.produtos.produto_schema import ProdutoIn
from sqlalchemy.orm import Session
from src.repository.produto.produto_repositorio import ProdutoRepositorio

class HandlerProduto:


    def __init__(self, produto: ProdutoIn, db: Session):
        self.produto = produto
        self.db = db

    async def chamar_repositorio_para_criar(self):
        criar_produto = ProdutoRepositorio(self.produto, self.db)
        return await criar_produto.criar_produto_respositorio()