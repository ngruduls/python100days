import requests

APP_ID = "9ea1820c"
API_KEY = "94b4986f3bc5f47f610cfe0ed3104511"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("what did you do (exercise)?")

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
print(result)