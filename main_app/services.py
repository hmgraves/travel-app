import os
import requests


def get_temptimezone(city):
    geocoding = requests.post(
        f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={os.getenv('DO_ACCESS_TOKEN')}")
    transgeocodes = geocoding.json()
    lat = transgeocodes["results"][0]["geometry"]["location"]["lat"]
    lon = transgeocodes["results"][0]["geometry"]["location"]["lng"]
    allWeatherDataJson = requests.post(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv('DO_ACCESS_TOKEN2')}")
    allWeatherData = allWeatherDataJson.json()
    temperatureKelvins = allWeatherData["main"]["temp"]
    temperatureF = int((temperatureKelvins-273.15)*9/5+32)

    city_weather = allWeatherData["weather"][0]["description"]
    return temperatureF


def weather_description(city):
    geocoding = requests.post(
        f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={os.getenv('DO_ACCESS_TOKEN')}")
    transgeocodes = geocoding.json()
    lat = transgeocodes["results"][0]["geometry"]["location"]["lat"]
    lon = transgeocodes["results"][0]["geometry"]["location"]["lng"]
    allWeatherDataJson = requests.post(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv('DO_ACCESS_TOKEN2')}")
    allWeatherData = allWeatherDataJson.json()
    city_weather = allWeatherData["weather"][0]["description"]
    return city_weather
