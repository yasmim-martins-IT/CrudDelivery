from fastapi import APIRouter

order_router = APIRouter(prefix="/order" , tags= ["order"])

@order_router.get("/") #um decorator que atribui uma funcionalidade nova para a função
async def listar_pedidos() :
  return