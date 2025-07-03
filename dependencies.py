#as dependencias das rotas serão criadas aq
from sqlalchemy.orm import sessionmaker
from models import db

def criar_sessao () :
  try:
    #cria as sessões no banco de dados
    Session = sessionmaker(bind=db)
    session = Session() #cria uma INSTANCIA da classe sessão
  
    yield session #ele não encerra a função porém ele retorna um valor para a função.
  finally :
    #o finally executa independente do que acontecer
    
    session.close() #fecha a sessão para o usuario