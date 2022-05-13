from datetime import datetime
import json
import re
import requests
from typing import Dict, List
import settings


def parsing(dict_: Dict = None) -> List:
	"""
	Собирает данные об отелях и передает боту
	:param dict_: Dict
	:return: List
	"""
	locations_search_url = settings.URLS[0]
	querystring = {"query": dict_.get('city')}
	locations_search_response = requests.request(
		"GET",
		locations_search_url,
		headers=settings.HEADERS,
		params=querystring
	)
	locations_search_data = json.loads(locations_search_response.text)
	locations_search_result = recursion_locations_search(locations_search_data, dict_)

	list_hotels_url = settings.URLS[1]
	if dict_['range_price']:
		querystring = {
			"destinationId": locations_search_result[1],
			"checkIn": dict_['check_in'],
			"checkOut": dict_['check_out'],
			"priceMin": dict_['range_price'][0],
			"priceMax": dict_['range_price'][1],
			"sortOrder": 'DISTANCE_FROM_LANDMARK',
		}
	else:
		querystring = {
			"destinationId": locations_search_result[1],
			"checkIn": dict_['check_in'],
			"checkOut": dict_['check_out']
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
	if list_hotels_result == []:
		return list_hotels_result
	else:
		if dict_.get('command') == 'lowprice':
			list_hotels_result = list_hotels_result[:int(dict_.get('amount'))]
		elif dict_.get('command') == 'highprice':
			list_hotels_result = list_hotels_result[-(int(dict_.get('amount'))):]
		elif dict_.get('command') == 'bestdeal':
			list_hotels_result = sort_bestdeal(list_hotels_result, dict_)
			if len(list_hotels_result) >= int(dict_.get('amount')):
				list_hotels_result = list_hotels_result[:int(dict_.get('amount'))]

		if not int(dict_.get('photo_amount')) == 0:
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
				photos_result = photos_result[:int(dict_.get('photo_amount'))]
				photos_list.append(photos_result)
			else:
				pass

		if list_hotels_result == []:
			return list_hotels_result
		else:
			list_info = [list() for _ in range(len(list_hotels_result))]
			for i in list_hotels_result:
				list_info[list_hotels_result.index(i)].append(i.get("name"))
				list_info[list_hotels_result.index(i)].append(i.get("address").get("streetAddress"))
				list_info[list_hotels_result.index(i)].append(i.get("landmarks")[0].get("distance"))
				list_info[list_hotels_result.index(i)].append(i.get("ratePlan").get("price").get("current"))
				if i.get("ratePlan").get("price").get("fullyBundledPricePerStay", ''):
					ppd = re.search(r'\$\d*\W*\d*', i.get("ratePlan").get("price").get("fullyBundledPricePerStay", '')).group()
					#print(ppd)
					list_info[list_hotels_result.index(i)].append(ppd)
				if not dict_.get('photo_amount') == 0:
					list_info[list_hotels_result.index(i)].extend(photos_list[list_hotels_result.index(i)])
				else:
					pass
			logging(list_info, dict_)

			return list_info

def sort_bestdeal(list_: List, dict_: Dict):
	"""
		Собирает список отелей для команды bestdeal
		:param list_: List
		:return: List
		"""
	range_distance = float(dict_.get('range_distance'))
	list_res = []
	p = r'\d*.\d*'
	for i in list_:
		s = i.get("landmarks")[0].get("distance")
		# print(s)
		# print(float(re.search(r'\d*.\d*', i.get("landmarks")[0].get("distance")).group()))
		if float(re.search(p, str(s)).group()) < range_distance:
			list_res.append(i)
			print(list_res)
	return list_res

def recursion_locations_search(data_: Dict, dict_: Dict) -> List:
	"""
	Определяет город, возвращает id города.
	:param data_: Dict
	:param dict_: Dict
	:return: List
	"""
	for i, j in data_.items():
		if isinstance(j, list):
			result = recursion_locations_search(j[0], dict_)

			return result

		if i == 'name' and j.isupper() == dict_.get('city').isupper():
			list_res = [data_.get('name'), data_.get('destinationId')]

			return list_res

def recursion_list_hotels(data_: Dict) -> List:
	"""
	Собирает список отелей
	:param data_: Dict
	:return: List
	"""
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
	"""
	Собирает список фото
	:param data_: Dict
	:return: List
	"""
	list_photos = []
	for i in data_.get('hotelImages'):
		url = i.get('baseUrl').split('{size}')
		url = 'z'.join(url)
		list_photos.append(url)

	return list_photos

def logging(list_: List, dict_: Dict) -> None:
	amount = len(list_)
	with open('log.txt', 'a', encoding='utf-8') as log_file:
		log_file.write('\n')
		log_file.write('{}\n'.format(datetime.utcnow()))
		log_file.write('{}\n'.format(dict_.get('command')))
		if list_ == []:
			log_file.write('{}\n{}\nЯ не смог ничего найти\n'.format(datetime.utcnow(), dict_.get('command')))
		else:
			log_file.write('{}\n{}\nЯ смог найти {} из {} отелей\n'.format(
				datetime.utcnow(), dict_.get('command'), amount, dict_.get('amount'))
			)
			if '$' in list_[0][4]:
				for i in range(amount):
					log_file.write(
						'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
						'цена за ночь - {price}, стоимость за указанные даты - {price_for_all}, {photos}\n'.format(
							name=list_[i][0],
							street=list_[i][1],
							distance=list_[i][2],
							price=list_[i][3],
							price_for_all=list_[i][4],
							photos=', '.join(list_[i][5:])
						))
			else:
				for i in range(amount):
					log_file.write(
						'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
						'цена за ночь - {price}, {photos}'.format(
							name=list_[i][0],
							street=list_[i][1],
							distance=list_[i][2],
							price=list_[i][3],
							photos=', '.join(list_[i][4:])
						))


if __name__ == '__main__':

	parsing()