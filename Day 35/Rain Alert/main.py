import requests
from twilio.rest import Client


ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "6ea05a98207e22f0ac86a284fe799dc5"

account_sid = "ACfbf6a87f61a91c812fc45d6bb00f4df7"
auth_token = "cca8b5ac57a9c8253ad8d81d96300d83"


parameters = {
    "lat": 23.810331,
    "lon": 90.412521,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
}


response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_data = weather_data
next_12_hourly_weather_data = weather_data["hourly"][:12]

will_rain = False
for weather in next_12_hourly_weather_data:
    if weather["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Hey, Shahjalal. It's going to rain. Remember to bring Umbrella.",
            from_="+19894398341",
            to="+971589196282"
        )

    print(message.status)
