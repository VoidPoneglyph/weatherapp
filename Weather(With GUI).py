import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city_name, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': city_name,
        'aqi': 'no'
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        location = data['location']
        current = data['current']
        return {
            'Location': location['name'],
            'Temperature': current['temp_c'],
            'Humidity': current['humidity'],
            'Description': current['condition']['text'],
            'Wind Speed': current['wind_kph']
        }
    else:
        return None

def show_weather():
    city = city_entry.get()
    if city:
        api_key = 'fe5ece531c06400aa58112348240910' 
        weather_data = get_weather(city, api_key)
        
        if weather_data:
            result = (
                f"Weather in {weather_data['Location']}:\n"
                f"Temperature: {weather_data['Temperature']}°C\n"
                f"Humidity: {weather_data['Humidity']}%\n"
                f"Description: {weather_data['Description']}\n"
                f"Wind Speed: {weather_data['Wind Speed']} km/h"
            )
            messagebox.showinfo("Weather Information", result)
        else:
            messagebox.showerror("Error", "City not found or API request failed.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")


root = tk.Tk()
root.title("Weather App")


city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()


get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.pack()

root.mainloop()
