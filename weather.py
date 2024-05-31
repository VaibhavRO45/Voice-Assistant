import requests
from ss import *

Key2 = "b792ca82ff5252b48e49592231db350f"

api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid='+Key2
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature

    return ar
'''arr = news()
print(arr)'''
def des():
    description = json_data["weather"][0]["description"]
    return description

print(temp())
print(des())