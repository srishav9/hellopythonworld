#https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/

import requests
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters)

py_data = json.loads(iTunes_response.text)
print(iTunes_response.url)
for r in py_data['results']:
    print(r['trackName'])
