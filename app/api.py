import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from modelo_regressao.predicao import predizer

from app import __version__, schemas
from app.config import settings

# APIRouter é uma classe que separa as operações de caminho de um submódulo do programa
# Mantendo-as na mesma aplicação de API. Documentação sobre o uso de APIRouter:
# https://fastapi.tiangolo.com/tutorial/bigger-applications/ 
api_router = APIRouter()


# Endpoint que exibe dados do projeto
# .get() é uma operação que corresponde a um método HTTP
# executada no caminho /health
@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version="1.2.1"
    )

    return health.dict()


# No caminho /predict, postar (método HTTP) a predição com base no exemplo da seção schemas
@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.MultipleHouseDataInputs) -> Any:
    """
    Predizer amostra exemplo de imóveis em São Paulo - SP
    """
    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    logger.info(f"Predizendo amostra: {input_data.inputs}")
    results = predizer(dados_entrada=input_df)

    logger.info(f"Resultados predição: {results.get('predicoes')}")

    return results
