from pprint import pprint
import requests

SHEETY_SHEET_ENDPOINT = "https://api.sheety.co/b87af8516a599340e23a081d45078290/flightData/sheet1"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """
        2. Use the Sheety API to GET all the data in that sheet and print it out.
        """
        response = requests.get(url=SHEETY_SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["sheet1"]
        """3. Try importing pretty print and printing the data out again using pprint().
        pprint(data)
        """
        return self.destination_data

    """
    6. In the DataManager Class make a PUT request and use the row id  from sheet_data to update the Google Sheet with the IATA codes. (Do this using code).
    """

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_SHEET_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
