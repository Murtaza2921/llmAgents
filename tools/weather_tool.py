import requests

def fetch_weather(city):
    api_url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return f"The weather in {city} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}."
    return "Unable to fetch weather data."
