import requests
import json

url_3 = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
querystring_3 = {"id": "561017"}
headers_3 = {
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    "X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
}
response_3 = requests.request("GET", url_3, headers=headers_3, params=querystring_3)
# print(response_3.text)
data_3 = json.loads(response_3.text)
with open('Folder/Photos.json', 'w') as photos:
    json.dump(data_3, photos, indent=4)
