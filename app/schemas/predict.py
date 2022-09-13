from typing import Any, List, Optional

from pydantic import BaseModel
from modelo_regressao.processamento.validacao import HouseDataInputSchema

# Modelo pydantic para resultados da predição
class PredictionResults(BaseModel):
    predicoes: List[float]
    versao: str

# Esquema de dados de entrada para predição
class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                      "area": 125.0,
                      "quartos": 4.0,
                      "banheiros": 3.0,
                      "vagas": 2.0,
                      "V001": 142.0,
                      "V002": 493.0,
                      "V003": 3.47,
                      "V004": 3.06,
                      "V005": 805.13,
                      "V006": 769188.78,
                      "V007": 1011.75,
                      "V008": 757433.42,
                      "V009": 518.77,
                      "V010": 426672.78,
                      "V011": 858.51,
                      "V012": 414378.88
                    }
                ]
            }
        }
