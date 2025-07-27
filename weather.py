import requests
from tkinter import *

def get_weather():
    city = city_entry.get()
    api_key = 'be07373d2d5e4cc77b8af0e826d71016'  # 🔁 Replace with your actual OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        if data['cod'] == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            result = f"🌤️ Weather: {weather}\n🌡️ Temperature: {temp}°C\n💧 Humidity: {humidity}%\n💨 Wind Speed: {wind_speed} m/s"
        else:
            result = "❌ City not found!"
    except:
        result = "⚠️ Error retrieving data."

    result_label.config(text=result)

# GUI setup
app = Tk()
app.title("Weather App")
app.geometry("400x300")
app.configure(bg="#87ceeb")

Label(app, text="Enter City Name", font=("Arial", 14, "bold"), bg="#87ceeb").pack(pady=10)
city_entry = Entry(app, font=("Arial", 14))
city_entry.pack()

Button(app, text="Get Weather", command=get_weather, font=("Arial", 12, "bold"), bg="#1e90ff", fg="white").pack(pady=10)

result_label = Label(app, text="", font=("Arial", 12), bg="#87ceeb", justify=LEFT)
result_label.pack(pady=20)

app.mainloop()
