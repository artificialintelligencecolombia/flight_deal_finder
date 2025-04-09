import os
from dotenv import load_dotenv
import requests

load_dotenv() # loads environment variables from .env file

class DataManager:
    def __init__(self) -> None:
        """Reads the base Sheety API URL and token. Prepares authorization headers. Initializes two empty data dicts. Validates that required environment variables exist."""
        self.base_url = os.getenv("BASE_SHEETY_URL")
        self.auth_token = os.getenv("SHEETY_AUTH_TOKEN")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
        }
        self.destination_data = {}
        self.update_data = {}
        
        if not self.base_url or not self.auth_token:
            raise ValueError("Missing environment variables")
        
    def get_data(self) -> dict:
        """Performs a GET request to the Sheety API. Stores the result in self.destination_data. Returns the JSON payload."""
        try:
            response = requests.get(url=self.base_url, headers=self.headers)
            response.raise_for_status()
            self.destination_data = response.json()    
            return self.destination_data
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(f"Error fetching data: {e}") from e
        
    def update_destination_code(self, row_id, iata_code) -> None:
        """Iterates through the destination_data object(?)."""
        new_data = {
            "sheet1": {
                "iataCode": iata_code
            }
        }
    
        try:
            put_url = f"{self.base_url}/{row_id}"  # Build PUT request URL
            put_response = requests.put(url=put_url, headers=self.headers, json=new_data)
            put_response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(f"Error updating data: {e}")
            
        


