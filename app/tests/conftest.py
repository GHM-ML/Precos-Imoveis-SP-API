from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from modelo_regressao.config.core import config
from modelo_regressao.processamento.gerenciador_dados import carregar_dataset

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    return carregar_dataset(nome_arq=config.app_config.arquivo_teste)


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
