import os

from supabase import Client, create_client
from supabase.client import ClientOptions

def pegar_client_supabase():
    try:
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")

        supabase: Client | None = None
        supabase = create_client(
            url, 
            key,
            options=ClientOptions(
                postgrest_client_timeout=10,
                storage_client_timeout=10,
                schema="public"
            )
        )

        if supabase is None:
            raise RuntimeError("Supabase não inicializado")

        yield supabase
    finally:
        supabase = None
