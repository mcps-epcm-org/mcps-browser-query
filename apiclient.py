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
        self.headers = {
            "Accept": "application/json, text/plain, /",
            "Referer": "https://rgc-mcps.regeneron.com/",
            "x-api-key": "pHBUpmf3hE2d9LKHQvgLY2LKMmW1Cns15E8JDsNn",
        }

    def fetch_data(self, endpoint: str) -> ResponseModel:
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return ResponseModel(data=response.json())
