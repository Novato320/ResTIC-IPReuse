from fastapi import APIRouter, Depends
from supabase import Client
from src.dependencies.banco_dependencies import pegar_client_supabase

router = APIRouter(prefix="/catalogo", tags=["Catalogo"])

@router.get("/")
def get_ips(banco:Client = Depends(pegar_client_supabase)):
    table = "ip_core"
    select = "*"

    response = (
        banco.table(table)
        .select(select)
        .execute()
    )

    #print(response)
    return response


@router.get("/{ip_id}")
def get_ip(ip_id: int, banco:Client = Depends(pegar_client_supabase)):
    table = "ip_core"
    select = "*"

    # id é chave primaria, logo o retorno é unico
    # single tranforma o retorno de lista[] em um unico objeto/dicionario{}
    response = (
        banco.table(table)
        .select(select)
        .eq("id", ip_id)
        .single()
        .execute()
    )

    # print(response)
    return response
