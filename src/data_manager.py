import os
from dotenv import load_dotenv
import requests

load_dotenv()

class DataManager:
    def __init__(self):
        self.base_url = os.getenv("BASE_SHEETY_URL")
        self.auth_token = os.getenv("SHEETY_AUTH_TOKEN")
        self.destination_data = {}
        
        if not self.base_url or not self.auth_token:
            raise ValueError("Missing environment variables")
        
    def get_data(self) -> dict:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
        }

        try:
            response = requests.get(url=self.base_url, headers=headers)
            response.raise_for_status()
            self.destination_data = response.json()    
            return self.destination_data
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(f"Error fetching data: {e}") from e


