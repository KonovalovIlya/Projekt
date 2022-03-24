import json
import re

import requests

# data: dict
def parsing(dict):
	url = "https://hotels4.p.rapidapi.com/locations/v2/search"
	querystring = {"query":"new york","locale":"en_US","currency":"USD"}
	headers = {
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
		"X-RapidAPI-Key": "7fa207022cmsh412a4ad33fcf0b9p16a1a3jsn22b953c844ee"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	return 'А вот и результат'

if __name__ == '__main__':

	parsing(dict)