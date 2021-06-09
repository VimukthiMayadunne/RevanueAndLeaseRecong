import json
import requests

url = "http://127.0.0.1:5000/getTreatment"

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

def send_request(data):
    data_json = json.dumps(data)
    print(data_json)
    response = requests.request("POST", url, data=data_json, headers=headers)
    print(response.text)
