import requests
from datetime import datetime

USERNAME = "shahjalalhazari"
TOKEN = "sdfsgsdfgsd"
GRAPH_ID = "graph01"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"


""" CREATE USER """
user_config = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_config)
# print(response.text)


""" CREATE GRAPH """
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


""" POST PIXELA """
today = datetime.now()

post_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
post_value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km did you run today?")
}

response = requests.post(url=post_endpoint, json=post_value_config, headers=headers)
print(response.text)


"""" UPDATE PIXELA """
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_pixela_config = {
    "quantity": "9.85"
}

# response = requests.put(url=update_pixela_endpoint, json=update_pixela_config, headers=headers)
# print(response.text)


""" DELETE PIXELA """
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
