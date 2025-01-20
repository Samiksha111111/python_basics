import requests

def get_weather_data(city_name):
    url = "https://api.open-meteo.com/v1/forecast"
    city_order= {
        "kathmandu" : (27.7103, 85.3222),
        "pokhara" : (28.2096, 83.9856),
        "janakpur" : (26.7271, 85.9407)
    }
    if city_name.lower() in city_order:
        latitude, longitude = city_order[city_name.lower()]
    else:
        print(f"City '{city_name}' not found.")
        return
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': 'true'
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Fetched successfully!\n")
        # Parse the JSON response
        data = response.json()
        current_weather = data.get('current_weather', {})

        print(f"City name: {city_name}")
        print(f"Temperature: {current_weather.get('temperature')} degree Celsius")
        print(f"Weather description: {current_weather.get('weathercode')}")
        print(f"Wind Speed: {current_weather.get('windspeed')}")
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")

city_name = input("Enter city name: ")
get_weather_data(city_name)
