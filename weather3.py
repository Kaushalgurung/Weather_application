import tkinter as tk
import requests
import time

def getWeather(self):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=23bd898d5ada146d2b8d614b2e6acaee"

    json_data = requests.get(api).json()
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))


    # Suggest food based on temperature
    if temp < 10:
        suggestion = "It's cold outside, how about some soup or stew?"
    elif temp < 20:
        suggestion = "It's chilly outside, how about some pasta or pizza?"
    elif temp < 30:
        suggestion = "It's warm outside, how about some salad or sandwiches?"
    else:
        suggestion = "It's hot outside, how about some ice cream or smoothies?"

    # Update the labels
    condition = json_data['weather'][0]['main']
    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset+"\n" + suggestion
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather and Food Recommendation App")

f = ("poppins", 15, "bold")
t= ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t) 
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
