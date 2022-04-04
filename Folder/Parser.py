import json
import re
import requests
from typing import Dict, List


# data: dict
def parsing(dict_: Dict = None) -> List:
	url_1 = "https://hotels4.p.rapidapi.com/locations/v2/search"
	querystring_1 = {"query":"new york","locale":"en_US","currency":"USD"}
	headers_1 = {
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
		"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
	}
	response_1 = requests.request("GET", url_1, headers=headers_1, params=querystring_1)
	data_1 = json.loads(response_1.text)
	result_1 = recursion(data_1, dict_)

	url_2 = "https://hotels4.p.rapidapi.com/properties/list"
	querystring_2 = {
		"destinationId": result_1[1], "pageNumber": "1", "pageSize": "25", "checkIn": dict_['check_in'],
		"checkOut": dict_['check_out'], "adults1": "1", "sortOrder": "PRICE", "locale": "en_US", "currency": "USD"
	}
	headers_2 = {
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
		"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
	}
	response_2 = requests.request("GET", url_2, headers=headers_2, params=querystring_2)
	data_2 = json.loads(response_2.text)
	result_2 = recursion_2(data_2)
	result_2 = result_2[:int(dict_.get('amount'))]

	url_3 = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
	querystring_3 = {"id": "1178275040"}
	headers_3 = {
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
		"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
	}
	response_3 = requests.request("GET", url_3, headers=headers_3, params=querystring_3)
	# print(response_3.text)
	data_3 = json.loads(response_3.text)
	with open('Photos.json', 'w') as photos:
		json.dump(response_3.text, photos, indent=4)

	# print(result_2)
	list_2 = [list() for _ in range(int(dict_.get('amount')))]
	for i in result_2:
		list_2[result_2.index(i)].append(i.get("name"))
		list_2[result_2.index(i)].append(i.get("address").get("streetAddress"))
		list_2[result_2.index(i)].append(i.get("landmarks")[0].get("distance"))
		list_2[result_2.index(i)].append(i.get("ratePlan").get("price").get("current"))
		list_2[result_2.index(i)].append(
			re.search(r'\$\d{3}', i.get().get("price").get("fullyBundledPricePerStay")).group()
		)
	# print(list_2)
	return list_2
	# return recursion(data_1)


def recursion(data_: Dict, dict_: Dict) -> List:
	for i, j in data_.items():
		if isinstance(j, list):
			result = recursion(j[0], dict_)
			return result
		if i == 'name' and j.isupper() == dict_.get('city').isupper():
			list_res = [data_.get('name'), data_.get('destinationId')]
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
			return data_.get(i)


if __name__ == '__main__':

	parsing()