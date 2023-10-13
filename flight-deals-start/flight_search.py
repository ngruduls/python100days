import requests
#https://api.tequila.kiwi.com/locations/query?term=Paris&locale=en-US&location_types=city&limit=1&active_only=true
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "MD5gzBYY0VzDhKA6bx8SRgWtIpe-atzL"

class FlightSearch:

    def get_destination_code(self, city_name):
        print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = { "apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city", "limit": 1, "active_only": "true"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        result_code = response.json()["locations"][0]["code"]
        return result_code