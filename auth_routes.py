from fastapi import APIRouter , Depends #depends cria as dependencias nas rotas
from models import Usuario 
from dependencies import criar_sessao

auth_router = APIRouter(prefix= "/auth", tags=["auth"] ) #cria o roteador das rotas colocando o prefixo padrão para todas as rotas, tags é pra organizar na documentação com o nomezinho

@auth_router.get("/")
async def autenticar() :
  return {"mensagem" : "rota padrão autentificar"}

@auth_router.post("/criar_conta")
async def criar_conta(email:str , senha : str, nome : str , session =Depends(criar_sessao) ) :
  #cadastra os usuario
  
  usuario = session.query(Usuario).filter(Usuario.email ==email).first() #procura todos os usuarios com o mesmo email que no parametro

  if usuario :
    return {"já existe um usuario com essse e-mail"}
  else :
    novo_usuario = Usuario(nome , email , senha) #cria uma instancia da classe usuario
    
    session.add(novo_usuario) #adiciona o novo usuario
    
    #commitando no banco de dados
    session.commit()
    
    return {"usuario criado com sucesso"}
    


