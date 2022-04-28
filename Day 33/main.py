import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)

if response.status_code == 404:
    raise Exception("That resource dose not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data.")

"""It's difficult to remember all of the Status Code and work on these one by one.
Better if we use Build-In Status Checker."""
print(response.raise_for_status())

# Display the actual data
data = response.json()
print(data)
# Get ISS current position
position = data["iss_position"]
print(position)
# Get longitude and latitude of ISS current position
longitude = data["iss_position"]["longitude"]
latitude = position["latitude"]
print(f"longitude: {longitude}, latitude: {latitude}")


# Use API with parameters
MY_LAT = 25.204849
MY_LNG = 55.270782

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 1
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

"""
By default, time formate is 12 Hours.
If we want 24 Hours time formate than we have pass one more parameter called "formatted"
and it should be 0. by default, formatted is 1. 
"""
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)