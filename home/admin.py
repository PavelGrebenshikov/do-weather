from django.contrib import admin
from .models import CityWeather

# Register your models here.

@admin.register(CityWeather)
class CityWeatherAdmin(admin.ModelAdmin):
    pass
