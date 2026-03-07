from ..database.database_supabase import consultar_banco
from ..controllers import catalogo_controller

from fastapi import APIRouter

router = APIRouter(prefix="/catalogo", tags=["Catalogo"])

@router.get("/")
def get_ips():
    resultado = consultar_banco("ip_core, *")
    print(resultado)
    return [{"id": "124352", "nome": "alfonso"},{"id": "122", "nome": "juh"},{"id": "352", "nome": "rone"}]


@router.get("/{ip_id}")
def get_ip(ip_id: int):
    return {"id": "352", "nome": "rone"}
