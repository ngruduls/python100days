import requests
from datetime import datetime

USERNAME = "nauris"
TOKEN = "nauris123fjj4414ff44fafh4"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading graph",
    "unit": "pages",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# yesterday = datetime(year=2023, month=9, day=23)
today = datetime.now()
print(today.strftime("%Y%m%d"))

#/v1/users/<username>/graphs/<graphID>
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230924"
# response = requests.put(url=update_endpoint, json=pixel_data, headers=headers)
# print(response.text)
