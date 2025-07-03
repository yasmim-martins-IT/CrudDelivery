#as dependencias das rotas serão criadas aq
from sqlalchemy.orm import sessionmaker
from models import db

def criar_sessao () :
  #cria as sessões no banco de dados
  Session = sessionmaker(bind=db)
  session = Session() #cria uma INSTANCIA da classe sessão
  
  return session