import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "z5ScDkNiQED7nse2EpJ9LPBK04vsFeLv"

tomorrow = datetime.now() + timedelta(1)
next_180_days = tomorrow + timedelta(180)
next_7_days = tomorrow + timedelta(7)
next_28_days = tomorrow + timedelta(28)


class FlightData:

    def __init__(self):
        self.date_from = tomorrow.strftime("%d/%m/%Y")
        self.date_to = next_180_days.strftime("%d/%m/%Y")
        self.return_from = next_7_days.strftime("%d/%m/%Y")
        self.return_to = next_28_days.strftime("%d/%m/%Y")

    def flight_data(self):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "fly_from": "DXB",
            "fly_to": "PAR",
            "date_from": self.date_from,
            "date_to": self.date_to,
            "return_from": self.return_from,
            "return_to": self.return_to,
            "flight_type": "round",
            "curr": "AED",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
        result = response.json()
        print(result)


flight_data = FlightData
