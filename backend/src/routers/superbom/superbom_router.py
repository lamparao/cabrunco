from fastapi import APIRouter, Depends
from src.schemas.produtos.produto_schema import ProdutoIn
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.handler.produto.handler_produto import HandlerProduto


superbom_router = APIRouter()


@superbom_router.post('', description='Adicionar produto', response_model=ProdutoIn)
async def cadastrar_produto(produto: ProdutoIn, db: Session = Depends(get_db)):
    handler_produto = HandlerProduto(produto, db)
    return await handler_produto.chamar_repositorio_para_criar()