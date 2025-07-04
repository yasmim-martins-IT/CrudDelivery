from fastapi import APIRouter , Depends , HTTPException #depends cria as dependencias nas rotas
from models import Usuario 
from dependencies import criar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix= "/auth", tags=["auth"] ) #cria o roteador das rotas colocando o prefixo padrão para todas as rotas, tags é pra organizar na documentação com o nomezinho

@auth_router.get("/")
async def autenticar() :
  return {"mensagem" : "rota padrão autentificar"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema : UsuarioSchema , session =Depends(criar_sessao) ) :
  #cadastra os usuario
  
  usuario = session.query(Usuario).filter(Usuario.email ==usuario_schema.email).first() #procura todos os usuarios com o mesmo email que no parametro
  
  if usuario :
    
    return {"já existe um usuario com essse e-mail"}
  
  else :
    senha_cryptografada = bcrypt_context.hash(usuario_schema.senha)#criando senha criptografada
    
    novo_usuario = Usuario(usuario_schema.nome , usuario_schema.email , senha_cryptografada, usuario_schema.ativo , usuario_schema.admin) #cria uma instancia da classe usuario
    
    session.add(novo_usuario) #adiciona o novo usuario
    
    #commitando no banco de dados
    session.commit()
    
    return ({"mensagem": f"usario cadastrado com sucesso {usuario_schema.email}"})
    


