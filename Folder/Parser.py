import json
import re
import requests
from typing import Dict, List
import settings


def parsing(dict_: Dict = None) -> List:
	'''
	Собирает данные об отелях и передает боту
	:param dict_: Dict
	:return: List
	'''
	locations_search_url = settings.URLS[0]
	querystring = {"query":dict_.get('city'),}
	locations_search_response = requests.request(
		"GET",
		locations_search_url,
		headers=settings.HEADERS,
		params=querystring
	)
	locations_search_data = json.loads(locations_search_response.text)
	locations_search_result = recursion_locations_search(locations_search_data, dict_)
	print(locations_search_result)

	list_hotels_url = settings.URLS[1]
	querystring = {
		"destinationId": locations_search_result[1], "checkIn": dict_['check_in'], "checkOut": dict_['check_out']
	}
	list_hotels_response = requests.request(
		"GET",
		list_hotels_url,
		headers=settings.HEADERS,
		params=querystring
	)
	list_hotels_data = json.loads(list_hotels_response.text)
	with open('list_hotels.json', 'w') as hotels:
		json.dump(list_hotels_data, hotels, indent=4)
	list_hotels_result = recursion_list_hotels(list_hotels_data)
	list_hotels_result = list_hotels_result[:int(dict_.get('amount'))]

	photos_url = settings.URLS[2]
	photos_list = []
	for i in list_hotels_result:
		querystring = {"id": i.get('id')}
		photos_response = requests.request(
			"GET",
			photos_url,
			headers=settings.HEADERS,
			params=querystring
		)
		photos_data = json.loads(photos_response.text)
		with open('Photos.json', 'w') as photos:
			json.dump(photos_data, photos, indent=4)
		photos_result = recursion_photos(photos_data)
		photos_result = photos_result[:dict_.get('foto_amount')]
		photos_list.append(photos_result)

	list_info = [list() for _ in range(int(dict_.get('amount')))]
	for i in list_hotels_result:
		list_info[list_hotels_result.index(i)].append(i.get("name"))
		list_info[list_hotels_result.index(i)].append(i.get("address").get("streetAddress"))
		list_info[list_hotels_result.index(i)].append(i.get("landmarks")[0].get("distance"))
		list_info[list_hotels_result.index(i)].append(i.get("ratePlan").get("price").get("current"))
		if i.get("ratePlan").get("price").get("fullyBundledPricePerStay", ''):
			ppd = re.search(r'\$\d*\W*\d*', i.get("ratePlan").get("price").get("fullyBundledPricePerStay", '')).group()
			print(ppd)
			list_info[list_hotels_result.index(i)].append(ppd)
		list_info[list_hotels_result.index(i)].extend(photos_list[list_hotels_result.index(i)])

	return list_info


def recursion_locations_search(data_: Dict, dict_: Dict) -> List:
	'''
	Определяет город, возвращает id города.
	:param data_: Dict
	:param dict_: Dict
	:return: List
	'''
	for i, j in data_.items():
		if isinstance(j, list):
			result = recursion_locations_search(j[0], dict_)

			return result

		if i == 'name' and j.isupper() == dict_.get('city').isupper():
			list_res = [data_.get('name'), data_.get('destinationId')]

			return list_res


def recursion_list_hotels(data_: Dict) -> List:
	'''
	Собирает список отелей
	:param data_: Dict
	:return: List
	'''
	for i, j in data_.items():
		if isinstance(j, dict):
			result = recursion_list_hotels(j)
			if result is None:
				pass
			else:

				return result

		if i == 'results':

			return data_.get(i)


def recursion_photos(data_: Dict) -> List:
	'''
	Собирает список фото
	:param data_: Dict
	:return: List
	'''
	list_photos = []
	for i in data_.get('hotelImages'):
		url = i.get('baseUrl').split('{size}')
		url = 'z'.join(url)
		list_photos.append(url)

	return list_photos


if __name__ == '__main__':

	parsing()