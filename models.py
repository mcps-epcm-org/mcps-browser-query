from pydantic import BaseModel
from typing import Any, Dict

class ResponseModel(BaseModel):
    """
    Modelo base para validar la respuesta de la API.
    """
    data: Dict[str, Any]
