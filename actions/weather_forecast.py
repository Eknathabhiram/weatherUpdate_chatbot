your_api_key= "f329a338e87c2cc40f4f81e03e35520a"
city = "Mumbai"
url="https://api.openweathermap.org/data/2.5/weather?q={city}&appid={your_api_key}"
# url="http://dataservice.accuweather.com/currentconditions/v1/{locationKey}"

# location_key = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey={your_api_key}&q=London"
import requests

response =requests.post(url)



def get_weather_data(city):
    return {"city": city, "temp": "37 Celsius", "climate": "Sunny"}