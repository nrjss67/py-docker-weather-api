import requests
import os


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris")
    print(r.json())

if __name__ == "__main__":
    get_weather()
