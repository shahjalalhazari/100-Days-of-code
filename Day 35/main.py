import requests


ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "6ea05a98207e22f0ac86a284fe799dc5"

parameters = {
    "lat": 25.204849,
    "lon": 55.270782,
    "exclude": "hourly",  # To exclude some parts of data from this API.
    "appid": API_KEY,
}


response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
print(response.json())