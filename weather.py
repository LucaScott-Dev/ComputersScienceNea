import requests
from dotenv import load_dotenv

def get_lat_lon(city_name, country_code, API_key):
    responce = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_key}')