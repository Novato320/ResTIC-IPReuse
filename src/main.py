from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv() # uma vezes executado adiciona os valores para todo o projeto

from .database.database_supabase import init_supabase, consultar_banco_users

app = FastAPI()

@app.on_event("startup")
def teste():
    init_supabase()

from .routers import catalogo_routes, login_routes,testes_routes

app.include_router(login_routes.router)
app.include_router(catalogo_routes.router)


app.include_router(testes_routes.router)

@app.get("/banco")
def banco():
    return consultar_banco_users()

"""
@app.on_event()
def teste():
    pass

@app.lifespan()
def teste():
    pass
"""