import os
import requests
from dotenv import load_dotenv

# Aggiunti gli import per simulare una specie di app 
import tkinter as tk
from tkinter import messagebox

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
            'lang': lang,
            # 'sys': sys
        }
        
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def format_weather(self, city):
        try:
            weather_data = self.get_weather(city)
            description = weather_data['weather'][0]['description'].capitalize()
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            temp_min = weather_data['main']['temp_min']
            temp_max = weather_data['main']['temp_max']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            return f"Meteo a {city}: {description}\n" \
                f"Temperatura: {temp}°C\n" \
                f"Percepiti: {feels_like}°C\n" \
                f"Temperatura minima e massima: {temp_min}°C - {temp_max}°C\n" \
                f"Umidità: {humidity}%\n" \
                f"Velocità del vento: {wind_speed} m/s"
        except requests.exceptions.HTTPError:
            return "Mannagg non funziona mica."

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Companion")
    
        root.config(bg="lightblue")
        # Crea un'istanza della classe WeatherCompanion
        self.client = WeatherCompanion()
        
        # Layout dell'interfaccia
        self.city_label = tk.Label(root, text="Inserisci il nome della città:")
        self.city_label.pack(pady=5)
        
        self.city_entry = tk.Entry(root, width=30)
        self.city_entry.pack(pady=10)
        
        self.get_weather_button = tk.Button(root, text="Mostra Meteo", command=self.display_weather)
        self.get_weather_button.pack(pady=20)
        
        self.weather_output = tk.Text(root, height=10, width=50)
        self.weather_output.pack(pady=10)
        self.weather_output.config(bg="Light Cyan")
        
    def display_weather(self):
        city = self.city_entry.get()
        if city:
            weather_info = self.client.format_weather(city)
            self.weather_output.delete(1.0, tk.END)  # Pulisce la Text Box
            self.weather_output.insert(tk.END, weather_info)  # Mostra i dati
        else:
            messagebox.showwarning("Input errato", "Per favore, inserisci una città.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
