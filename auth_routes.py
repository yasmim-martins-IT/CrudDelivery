from fastapi import APIRouter
from models import Usuario , db
from sqlalchemy.orm import sessionmaker 

auth_router = APIRouter(prefix= "/auth", tags=["auth"] ) #cria o roteador das rotas colocando o prefixo padrão para todas as rotas, tags é pra organizar na documentação com o nomezinho

@auth_router.get("/")
async def autenticar() :
  return {"mensagem" : "rota padrão autentificar"}

@auth_router.post("/criar_conta")
async def criar_conta(email:str , senha : str, nome : str) :
  #cadastra os usuario
  
  Session = sessionmaker(bind=db) #cria uma sessão no banco de dados
  session = Session()
  
  usuario = session.query(Usuario).filter(Usuario.email ==email).first() #procura todos os usuarios com o mesmo email que no parametro

  if usuario :
    return {"já existe um usuario com essse e-mail"}
  else :
    novo_usuario = Usuario(nome , email , senha) #cria uma instancia da classe usuario
    
    session.add(novo_usuario) #adiciona o novo usuario
    
    #commitando no banco de dados
    session.commit()
    
    return {"usuario criado com sucesso"}
    


