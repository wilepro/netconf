import requests
from rich import print

url = "https://api.restful-api.dev/objects"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)
result = response.json()
for item in result:
    if "Apple" in item["name"]:
        print(item["name"])
