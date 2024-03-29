import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "z5ScDkNiQED7nse2EpJ9LPBK04vsFeLv"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}

        response = requests.get(
            url=location_endpoint,
            headers=headers,
            params=query
        )
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
