import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Paris"

def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": CITY,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = data["current"]

        print(f"Paris, {data['location']['country']}")
        print(f"Local time: {data['location']['localtime']}")
        print(f"Temperature: {weather.get('temp_c')}")
        print(f"{weather['condition']['text']}")
        print(f"Wind speed: {weather.get('wind_kph')} km/h")

    except requests.exceptions.RequestException as e:
        print(f"Error taking weather data {e}")


if __name__ == "__main__":
    get_weather()
