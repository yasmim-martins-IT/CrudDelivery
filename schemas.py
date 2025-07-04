from pydantic import BaseModel
from typing import Optional 


#verifica tipagem deixando uma estrutura mais robusta
class UsuarioSchema(BaseModel) :
  nome : str
  email : str
  senha : str
  ativo : Optional[bool]
  admin : Optional[bool]
  
  class Config:
    #muda a forma que armazena não sendo mais uma lista
    from_attributes = True
    
class PedidoSchema(BaseModel) :
  id_usuario: int 
  
  class Config :
    
    from_attributes = True
  
  