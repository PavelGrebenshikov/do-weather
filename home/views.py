import requests
import json
from django.shortcuts import render
from django.conf import settings
from .models import CityWeather
# Create your views here.


def index(request):

    cities = CityWeather.objects.all()

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + settings.WEATHER_KEY

    weather_data = []

    for city in cities:
        response = requests.get(url.format(city))

        if response.status_code == 200:
            resp_dict = response.json()
            city_weather = {
            'name': resp_dict['name'], 
            'country': resp_dict['sys']['country'], 
            'temp': int(resp_dict['main']['temp']), 
            'temp_min': resp_dict['main']['temp_min'], 
            'temp_max': resp_dict['main']['temp_max'],
            'weather_main': resp_dict['weather'][0]['main'],
            'weather_desc': resp_dict['weather'][0]['description'],
            'weather_icon': resp_dict['weather'][0]['icon'],
            }

            weather_data.append(city_weather)
        else:
            return render(request, 'home/index.html', {"error_response": "Couldn't get a response"})
    return render(request, "home/index.html", {"city_weather" : weather_data})
