import requests
import json


res = dict()

req_1 = requests.get('https://www.breakingbadapi.com/api/')
data_1 = json.loads(req_1.text)
req_2 = requests.get(data_1['deaths'])
deaths = json.loads(req_2.text)
req_3 = requests.get(data_1['episodes'])
episodes = json.loads(req_3.text)

max = 0
for i in deaths:
    if i["number_of_deaths"] > max:
        max = i["number_of_deaths"]
        res['season'] = i['season']
        res['episode'] = i['episode']
        res['number_of_deaths'] = i["number_of_deaths"]
        res['death'] = i["death"]

for i in episodes:
    if int(i['season']) == res['season']:
        if int(i['episode']) == res['episode']:
            res['episode ID'] = int(i['episode_id'])

with open('result.json', 'w') as res_file:
    json.dump(res, res_file, indent=4)

print(res)
