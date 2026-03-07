from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/testes", tags=["Testes"])

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}

def funcao_qualquer():
    try:
        yield {"mensagem": "olá"} # com return ele não volta para essa função e o finally não executa
    finally:
        print("Acabou a função qualquer")

@router.get("/depedencia/{item_id}")
def get_item(item_id: int, dependencia = Depends(funcao_qualquer)):
    """
    Essa função usa o recurso de dependencias do fastapi
    """
    dict1 = {"id": item_id}
    dict2 = dependencia

    dict3 = dict1 | dict2
    dict4 = dict1.update(dict2) # muda o dict1 mas não salva no dict4
    dict5 = {**dict1, **dict2}

    print(dict3)
    print(dict4)
    print(dict5)

    return dict5

@router.get("/retorno/{dados}")
def codigos_retorno(nome:str, senha:str):
    """
    essa função muda o status code
    """
    if nome == "abc":
        raise HTTPException(status_code=400, detail="Não gosto de 'abc'")
    else:
        return {"mensagem": f"usuario {nome} e {senha} foi recebido"}

from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: Optional[str]
    senha: str
    """
    class Config:
        from_attributes = True # aparentemente relacionado ao sql alchemy, faz os dados virem como classe em vez de dicionario
    """

@router.post("/schema")
def com_schemas_post(usuario: UsuarioSchema):
    return {"mensagem": "recebido","nome": f"{usuario.nome}", "email": f"{usuario.email}", "senha": f"{usuario.senha}"}

# aparentemento chemas são para serem usados com Post
@router.get("/schema/{dados}")
def com_schemas_get(usuario: UsuarioSchema, numero: int):
    return {"numero": f"{numero}","mensagem": "recebido","nome": f"{usuario.nome}", "email": f"{usuario.email}", "senha": f"{usuario.senha}"}

"""
@router.on_startup()
def teste():
    print("Olá")

@router.on_event()
def teste():
    pass

@router.lifespan()
def teste():
    pass
"""
