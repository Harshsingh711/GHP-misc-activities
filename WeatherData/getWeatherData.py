import requests
import json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="

city1 = input("what is the first city you want to compare? ")
city2 = input("what is the second city you want to compare? ")


CITY1 = city1
CITY2 = city2
STATE = "GA"
COUNTRY = "US"

API_KEY = "8a9a78329c6ab165cb116d65ccce11a1"

URL1 = BASE_URL + CITY1 + "," + STATE + "," + COUNTRY + "&appid=" + API_KEY + "&units=metric"
URL2 = BASE_URL + CITY2 + "," + STATE + "," + COUNTRY + "&appid=" + API_KEY + "&units=metric"

response1 = requests.get(URL1)
response2 = requests.get(URL2)


if response1.status_code == 200 and response2.status_code == 200:
    #parse data
    data1 = response1.json()
    data2 = response2.json()
    main1 = data1['main']
    #get wind dictionary
    wind1 = data1['wind']
    windSpeed1 = wind1['speed']
    temperature1 = main1['temp']
    feelsLikeTemp1 = main1['feels_like']

    main2 = data2['main']
    wind2 = data2['wind']
    windSpeed2 = wind2['speed']
    temperature2 = main2['temp']
    feelsLikeTemp2 = main2['feels_like']



    print(city1 + ": ")
    print("temperature: " + str(temperature1) + " C")
    print("It feels like: " + str(feelsLikeTemp1) + " C")
    print("Wind Speed: " + str(windSpeed1) + " Km/H")

    print(city2 + ": ")
    print("temperature: " + str(temperature2) + " C")
    print("It feels like: " + str(feelsLikeTemp2) + " C")
    print("Wind Speed: " + str(windSpeed2) + " Km/H")
else:
    print(response1.status_code)
    print(response2.status_code)
    print("bad request")
