from fastapi import APIRouter , Depends 
from dependencies import criar_sessao
from schemas import PedidoSchema
from sqlalchemy.orm import Session

order_router = APIRouter(prefix="/order" , tags= ["order"])

@order_router.get("/") #um decorator que atribui uma funcionalidade nova para a função
async def listar_pedidos() :
  return

@order_router.post("/pedido") 
async def criar_pedido(pedidos_schema : PedidoSchema , session : Session = Depends(criar_sessao)) :
  pass