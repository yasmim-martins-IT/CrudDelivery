from fastapi import APIRouter

auth_router = APIRouter(prefix= "/auth", tags=["auth"] ) #cria o roteador das rotas colocando o prefixo padrão para todas as rotas, tags é pra organizar na documentação com o nomezinho

@auth_router.get("/")
async def autenticar() :
  return {"mensagem" : "rota padrão autentificar"}




