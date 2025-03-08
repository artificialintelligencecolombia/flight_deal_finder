import os
import requests
from dotenv import load_dotenv

load_dotenv()

AMADEUS_ACCESS_TOKEN = os.environ.get('AMADEUS_ACCESS_TOKEN')
AMADEUS_API_KEY = os.environ.get('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.environ.get('AMADEUS_API_SECRET')

params = {
    "grant_type": "client_credentials",
    "client_id": AMADEUS_API_KEY,
    "client_secret": AMADEUS_API_SECRET
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url=AMADEUS_ACCESS_TOKEN, data=params, headers=headers)
response.raise_for_status()

access_token = response.json()['access_token']
expiration_date = response.json()['expires_in']
print(f"Access token: {access_token}")
print(f"Expiration date: {expiration_date}")
