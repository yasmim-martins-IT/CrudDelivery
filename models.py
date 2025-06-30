from sqlalchemy import create_engine , Column , String , Integer , Boolean , ForeignKey , Float
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db") #conexão com o banco

#crua a base do banco de dados

Base = declarative_base()

#criar as classes/tabelas do banco
class Usuario(Base) :
  __tablename__ = "usuarios"
  
  id = Column("id", Integer, primary_key= True , autoincrement= True) #nome da coluna no banco e o tipo de dado que será armazenado
  nome = Column("nome", String , nullable=False) #não pode ser nulo
  email = Column("email", String)
  senha = Column("senha" ,String )
  ativo = Column("ativo" , Boolean)
  admin = Column("admin",Boolean, default= False) #dá para colocar um valor padrão do parametro
  
  def __init__(self, id , nome , email , senha, ativo = True , admin= False) :
    #cria o usuario no banco de dados
    self.id : int = id # coloquei uma validação a mais de tipo
    self.nome :str = nome
    self.email :str = email 
    self.senha : str = senha
    self.ativo : bool = ativo
    self.admin : bool = admin 
    
class Pedido(Base) :
  __tablename__ = "pedidos"
  
  ChoisesPedidos = (("PENDENTE", "PEDENTE"),("CANCELADO", "CANCELADO"), ("FINALIZADO", "FINALIZADO") )
  
  id = Column("id", Integer, primary_key= True , autoincrement= True)
  status = Column("status", String ,ChoiceType(choices=ChoisesPedidos)) #Campo com opções para a seleção
  usuario = Column("usuario" , ForeignKey("usuarios.id"))
  preco = Column("preco", Float)
  
  def __init__ (self, usuario , status = "PENDENTE" , preco = 0) :
    self.usuario = usuario
    self.status = status 
    self.preco = preco
  
class ItemPedido(Base) :
  __tablename__ = "itens_pedidos"
  
  SABORES = (("MUSARELA" , "MUSARELA"), ("LOMBO COM CATUPIRY","LOMBO COM CATUPIRY"), ("CALABRESA","CALABRESA" ))
  
  id = Column("id", Integer, primary_key= True , autoincrement= True)
  quantidade = Column("quantidade", Integer, default= 1 )
  sabor = Column("sabor" , String , ChoiceType(choices=SABORES)) 
  tamanho= Column("tamanho", String)
  preco_unitario = Column("preco_unitario" , Float)
  pedido = Column("pedido", ForeignKey("pedidos.id"))
  
  def __init__(self , quantidade , sabor , tamanho , preco_uniario , pedido) :
    self.quantidade = quantidade
    self.sabor = sabor
    self.tamanho = tamanho
    self.preco_unitario = preco_uniario
    self.pedido = pedido
    
    
#executa a criação dos metados do seu banco