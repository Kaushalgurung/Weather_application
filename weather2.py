import requests
import time

city = input("Enter city name: ")

api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=23bd898d5ada146d2b8d614b2e6acaee"

response = requests.get(api)

if response.status_code == 200:
    data = response.json()
    temperature = round(data["main"]["temp"] - 273.15, 1)
    description = data["weather"][0]["description"]
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(data['sys']['sunset'] - 21600))
    print(f"Temperature in {city}: {temperature}°C")
    print(f"Description: {description}")
    print(f"Pressure: {pressure}")
    print(f"Wind speed:{wind}")
    print(f"Humidity: {humidity}")
    print(f"Sunrise:{sunrise}")
    print(f"Sunset:{sunset}")

          

else:
    print("Error fetching weather information")