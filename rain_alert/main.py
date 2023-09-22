import requests
#https://api.openweathermap.org/data/2.5/weather?lat=56.9493977&lon=24.1051846&appid=0a362e118354c62b9f8ddab2e9f3f32f

owm_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "0a362e118354c62b9f8ddab2e9f3f32f"

weather_params = {
    "lat": 56.9493977,
    "lon": 24.1051846,
    "appid": api_key
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["weather"][0]["id"])

