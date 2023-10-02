import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/464e0305c4e96ea7d2620795c3df0634/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out
        response = requests.get(SHEETY_PRICES_ENDPOINT);
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    #6
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", #use row number
                json=new_data
            )
            print(response.text)