import tkinter as tk
import requests

API_KEY = "45838fafe187124ed21bd752022ad7dc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        result = f"City: {city.upper()}\nTemperature: {temp}°C\nCondition: {desc}\nHumidity: {humidity}%\nSpeed: {wind} m/s"
    else:
        result = "City not found. Please try again."
    result_label.config(text=result)
    city_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")
app.config(bg="lightblue")
tk.Label(app, text="Weather App", font=("Times New Roman", 20), bg="lightblue").pack(pady=10)
tk.Label(app, text="Enter City Name:", bg="lightblue").pack(pady=5)
city_entry = tk.Entry(app, width=30)
city_entry.pack()
tk.Button(app, text="Get Weather", command=get_weather).pack(pady=10)
result_label = tk.Label(app, text="", bg="lightblue")
result_label.pack(pady=10)
app.mainloop()