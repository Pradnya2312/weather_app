# weather_app
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']} %")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(f"Failed to get weather data: {data['message']}")

if __name__ == "__main__":
    api_key = "f5e2e093a72a964c70ebd0d0a222a067"
    city = "Pune"
    get_weather(api_key, city)
