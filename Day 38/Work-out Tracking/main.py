import os
import requests
from datetime import datetime


GENDER = "male"
WEIGHT_KG = 54
HEIGHT_CM = 171
AGE = 21

APP_ID = "MY_APP_ID"
API_KEY = "MY_API_KEY"

TOKEN = "MY_TOKEN"

USERNAME = "MY_USERNAME"
PASSWORD = "MY_PASSWORD"


# ENDPOINTs
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "SHEETY_ENDPOINT"

exercise_text = input("Which exercises you did? ")


bearer_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_paramas = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age":AGE
}

response = requests.post(exercise_endpoint, json=exercise_paramas, headers=bearer_headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            USERNAME,
            PASSWORD,
        )
    )

    print(sheet_response.text)
