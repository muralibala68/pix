import requests
import json
import sys


response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=beatles")

response_as_json = response.json()
#print(json.dumps(response_as_json, indent=2))

for result in response_as_json["results"]:
    print(result["trackName"])

