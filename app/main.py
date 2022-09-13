from typing import Any

from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from loguru import logger

from app.api import api_router
from app.config import settings, setup_app_logging

# configurar log tão cedo quanto possível
setup_app_logging(config=settings)

# A variável app será uma instância da classe FastAPI
# Este será o ponto de interação principal para criar toda a API
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Endpoint raiz da API
root_router = APIRouter()


# Mostra a resposta HTML definida na função index na página inicial (raiz) da API
@root_router.get("/")
def index(request: Request) -> Any:
    """Resposta HTML básica"""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Bem vindo(a) à API</h1>"
        "<div>"
        "Continue <a href='/docs'>aqui</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)

# incluir endpoints no app
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

# https://fastapi.tiangolo.com/tutorial/cors/
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


