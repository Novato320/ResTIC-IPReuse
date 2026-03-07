from fastapi import APIRouter, Depends
from supabase import Client
from src.dependencies.banco_dependencies import pegar_client_supabase

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/")
def home():
    """
    Essa é a rota padrão de autenticação da API
    """
    return {"mensagem": "Acessou rota padrão de autenticação"}

@router.post("/criar_conta")
def criar_conta(email: str, senha: str, banco:Client = Depends(pegar_client_supabase)):
    pass

@router.post("/logar")
def logar(email: str, senha: str, banco:Client = Depends(pegar_client_supabase)):
    
    response = (
    banco.table("users")
    .select("*")
    .eq("email", email)
    .single()
    .execute()
    )

    print(response)
    return response