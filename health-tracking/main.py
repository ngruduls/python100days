import os
import requests
from datetime import datetime

APP_ID = "9ea1820c"
API_KEY = os.environ.get("nutritionix_api_key")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/464e0305c4e96ea7d2620795c3df0634/workoutTracking/workouts"
TOKEN = os.environ.get("sheety_token")

exercise_text = input("what did you do (exercise): ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-type": "application/json"
}

parameters = {
 "query": exercise_text,
 "gender":"male",
 "weight_kg":72.5,
 "height_cm":178.00,
 "age":31
}


response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

#########################################
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Bearer " + TOKEN
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
