import json
import re
import requests


# data: dict
def parsing(dict_):
	url = "https://hotels4.p.rapidapi.com/locations/v2/search"
	querystring = {"query":"new york","locale":"en_US","currency":"USD"}
	headers = {
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
		"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	data_1 = json.loads(response.text)
	result_1 = recursion(data_1)
	url = "https://hotels4.p.rapidapi.com/properties/list"
	querystring = {
		"destinationId": result_1[1], "pageNumber": "1", "pageSize": "25", "checkIn": "2020-01-08",
		"checkOut": "2020-01-15", "adults1": "1", "sortOrder": "PRICE", "locale": "en_US", "currency": "USD"
	}
	headers = {
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
		"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
	}
	response_2 = requests.request("GET", url, headers=headers, params=querystring)
	data_2 = json.loads(response_2.text)
	result_2 = recursion_2(data_2)
	with open('list_hotels.json', 'w') as file:
		json.dump(result_2, file, indent=4)
	f = dict_['foto_amount']
	print(type(f))
	# result_2 = result_2[:int(dict_['foto_amount'])]
	# print(result_2)
	# list_2 = []
	# for i in result_2:
	# 	list_2.append(i['name'])
	# return list_2
	# return recursion(data_1)


def recursion(data_):
	for i, j in data_.items():
		if isinstance(j, list):
			result = recursion(j[0])
			return result
		if i == 'name':
			list_res = [data_['name'], data_['destinationId']]
			return list_res


def recursion_2(data_):
	for i, j in data_.items():
		if isinstance(j, dict):
			result = recursion_2(j)
			if result is None:
				pass
			else:
				return result
		if i == 'results':
			return data_[i]



if __name__ == '__main__':

	parsing(dict)