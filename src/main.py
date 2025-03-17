import os
import requests
from dotenv import load_dotenv
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheet_data = DataManager()
dataset = sheet_data.get_data()
# pprint(dataset)

for row in dataset['sheet1']:
    city_name = row['cityDestination']
    print(city_name)
    if row['iataCode'] == '':
        # updated_iata_code = FlightSearch.get_destination_code(city_name)
        print(row['iataCode'])
    # row['iataCode'] = updated_iata_code

#pprint(dataset)