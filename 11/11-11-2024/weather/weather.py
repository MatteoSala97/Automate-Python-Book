import os
import requests
from dotenv import load_dotenv

# link to the site
# https://openweathermap.org

# json da dove pesco i dati - rimpiazzare city_name e api_key con relative info
# http://api.openweathermap.org/data/2.5/weather?q=CITY_NAME&appid=YOUR_API_KEY&units=metric&lang=it 

## esempio di json ##    

'''
{
    "coord": {
        "lon": 13.2422,
        "lat": 46.0619
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "cielo sereno",
            "icon": "01d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 12.51,
        "feels_like": 10.91,
        "temp_min": 9.74,
        "temp_max": 13.53,
        "pressure": 1024,
        "humidity": 42,
        "sea_level": 1024,
        "grnd_level": 1006
    },
    "visibility": 10000,
    "wind": {
        "speed": 2.24,
        "deg": 0,
        "gust": 4.47
    },
    "clouds": {
        "all": 0
    },
    "dt": 1731336594,
    "sys": {
        "type": 2,
        "id": 2002431,
        "country": "IT",
        "sunrise": 1731304943,
        "sunset": 1731339595
    },
    "timezone": 3600,
    "id": 3165072,
    "name": "Udine",
    "cod": 200
}
'''

# load_dotenv()

# Verifica se l'API key è stata caricata - scommentare per controllare
# api_key = os.getenv('APPID')
# if api_key:
#     print('Loaded successfully.')

class WeatherCompanion:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('APPID')
        
        #controller su apikey - se esiste o no
        if not self.api_key:
            raise ValueError("API key non trovata. Crea un .env e incolla l'api key col nome di APPID")
        
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    #definisce i params
    def get_weather(self, city, lang='it'):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric' ,
            'lang': lang
        }
        
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def print_weather(self, city, lang='it'):
        try:
            weather_data = self.get_weather(city)
            print(f"Meteo a {city}: {weather_data['weather'][0]['description']}")
            print(f"Temperatura: {weather_data['main']['temp']}°C")
            print(f"Umidità: {weather_data['main']['humidity']}%")
            print(f"Velocità del vento: {weather_data['wind']['speed']} m/s")
        except requests.exceptions.HTTPError as http_err:
            print('Mannagg non funzia')

if __name__ == '__main__':
    client = WeatherCompanion()
    city = input('Inserisci il nome della città: ')
    client.print_weather(city)

