"""
apiclient.py

API 

"""
import os
from typing import Any, Dict
import requests
from models import ResponseModel

class APIClient:
    """
    Cliente para realizar consultas a la API.
    """
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.api_key = os.getenv("MCPS_BROWSER_API_KEY")
    
    def fetch_data(self, endpoint: str) -> ResponseModel:
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return ResponseModel(data=response.json())
