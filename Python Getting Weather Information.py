import requests
from pprint import pprint

API_Key = '0b9afb316a906fdd49feba981d7a341e'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)