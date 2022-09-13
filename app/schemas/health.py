from pydantic import BaseModel

# Esquema de descrição básica do app
class Health(BaseModel):
    name: str
    api_version: str
    model_version: str
