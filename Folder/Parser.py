import json
import re
import requests
from typing import Dict, List


# data: dict
def parsing(dict_: Dict = None) -> List:
	url = "https://hotels4.p.rapidapi.com/locations/v2/search"
	querystring = {"query":"new york","locale":"en_US","currency":"USD"}
	headers = {
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
		"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	data_1 = json.loads(response.text)
	result_1 = recursion(data_1, dict_)

	url = "https://hotels4.p.rapidapi.com/properties/list"
	querystring = {
		"destinationId": result_1[1], "pageNumber": "1", "pageSize": "25", "checkIn": dict_['check_in'],
		"checkOut": dict_['check_out'], "adults1": "1", "sortOrder": "PRICE", "locale": "en_US", "currency": "USD"
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
	result_2 = result_2[:3]
	# print(result_2)
	list_2 = [list() for _ in range(3)]
	for i in result_2:
		list_2[result_2.index(i)].append(i["name"])
		list_2[result_2.index(i)].append(i["address"]["streetAddress"])
		list_2[result_2.index(i)].append(i["landmarks"][0]["distance"])
		list_2[result_2.index(i)].append(i["ratePlan"]["price"]["current"])
		list_2[result_2.index(i)].append(
			re.search(r'\$\d{3}', i["ratePlan"]["price"]["fullyBundledPricePerStay"]).group()
		)
	# print(list_2)
	return list_2
	# return recursion(data_1)


def recursion(data_: Dict, dict_: Dict) -> List:
	for i, j in data_.items():
		if isinstance(j, list):
			result = recursion(j[0], dict_)
			return result
		if i == 'name' and j.isupper() == dict_['city'].isupper():
			list_res = [data_['name'], data_['destinationId']]
			return list_res


def recursion_2(data_: Dict) -> List:
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

	parsing()