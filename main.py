#para rodar o código , execute esse comando no terminal : uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

#importando os arquivos de rotas 

from auth_routes import auth_router
from order_routes import order_router

#incluindo as rotas

app.include_router(auth_router)
app.include_router(order_router ) 