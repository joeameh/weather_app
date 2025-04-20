import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("FORCAST_APIKEY")

def get_data(place, forcast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    data = get_data("Tokyo", 2,)
    print(get_data("Tokyo", 2,))
    dates = [date["dt_txt"].split(" ")[0] for date in data]
    print(dates)


