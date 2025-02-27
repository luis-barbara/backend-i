import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=pt_br"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data.get("main")
        weather = data.get("weather")[0]
        temperature = main.get("temp")
        description = weather.get("description")
        
        print(f"Clima em {city}:")
        print(f"Temperatura: {temperature}°C")
        print(f"Descrição: {description.capitalize()}")
        print('-' * 30)
    else:
        print(f"Falha ao obter dados para {city}. Código de status: {response.status_code}")

if __name__ == "__main__":
    cities = ['London', 'Paris', 'Tokyo']
    

    API_KEY = os.getenv('API_KEY')
    
    if not API_KEY:
        print("Chave de API não encontrada! Verificar o arquivo .env")
    else:
        for city in cities:
            fetch_weather(city, API_KEY)