import requests
from dataclasses import dataclass

API_Key = '008684c74ef8b04655b43caa50b10aaf'

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature : float

def get_lat_lon(city_name, API_Key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},&appid={API_Key}').json()
    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

def get_weather(lat, lon, API_Key, temp_units):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}&units={temp_units}').json()
    data = WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=response.get('main').get('temp')
    )
    
    return data

def main(city_name, temp_units):
    lat, lon = get_lat_lon('London', API_Key)
    WeatherData = get_weather(lat, lon, API_Key, temp_units)
    return WeatherData

if __name__ == "__main__":
    lat, lon = get_lat_lon('London', API_Key)
    print(get_weather(lat, lon, API_Key))