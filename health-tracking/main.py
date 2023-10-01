import json

import requests
from datetime import datetime

APP_ID = "9ea1820c"
API_KEY = "94b4986f3bc5f47f610cfe0ed3104511"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/464e0305c4e96ea7d2620795c3df0634/workoutTracking/workouts"

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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
