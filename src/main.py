
from data_manager import DataManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheet_data = DataManager()
flight_search = FlightSearch()
dataset = sheet_data.get_data()
# pprint(dataset)

for row in dataset['sheet1']:
    city_name = row['cityDestination']
    row_id = row['id']
    print(city_name)
    iata_code = flight_search.get_destination_code(city_name)
    sheet_data.update_destination_code(row_id, iata_code)
    

#pprint(dataset)