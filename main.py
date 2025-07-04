#para rodar o código , execute esse comando no terminal : uvicorn main:app --reload
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

#criptografando minhas senhas
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") #chave secreta armazenada na variavelde ambiente env

bcrypt_context =CryptContext(schemes=["bcrypt"], deprecated = "auto")#ele vai criptografar e ver se a senha bate com a do banco de dados


app = FastAPI()

#importando os arquivos de rotas 

from auth_routes import auth_router
from order_routes import order_router

#incluindo as rotas

app.include_router(auth_router)
app.include_router(order_router ) 