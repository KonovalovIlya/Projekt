import json
import re
import requests


# data: dict
def parsing(dict_: dict):
	url = "https://hotels4.p.rapidapi.com/locations/v2/search"
	querystring = {"query": "new york", "locale": "en_US", "currency": "USD"}
	headers = {
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
		"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)
	data_1 = json.loads(response.text)
	res = recursion(data_1)
	if res[0] in dict_.values():
		url = "https://hotels4.p.rapidapi.com/properties/list"
		querystring = {
			"destinationId": res[1], "pageNumber": "1", "pageSize": "25", "checkIn": "2020-01-08",
			"checkOut": "2020-01-15", "adults1": "1", "sortOrder": "PRICE", "locale": "en_US",
			"currency": "USD"
		}
		headers = {
			"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
			"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
		}
		response_1 = requests.request("GET", url, headers=headers, params=querystring)
		print(response_1.text)
		data_2 = json.loads(response_1.text)
		res_2 = recursion_2(data_2)
		print('res_2', res_2)


def recursion(structure):
	list_res = []
	for i, j in structure.items():
		if isinstance(j, list):
			for k in j:
				result = recursion(k)
				return result
		elif i == 'name':
			name = structure[i]
			list_res += [name, structure['destinationId']]
			return list_res


def recursion_2(structure):
	for i, j in structure.items():
		if isinstance(j, list):
			if i == "results":
				return j
		if isinstance(j, dict):
			result = recursion_2(structure[i])
			return result
		elif j is None:
			pass


data = dict()
data['city'] = 'New York'
parsing(data)
