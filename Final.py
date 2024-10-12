import requests
from tkinter import messagebox
import tkinter as tk

def get_weather_and_forecast(city_name,unit):
    api_key = 'fe5ece531c06400aa58112348240910'  
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        'key': api_key,
        'q': city_name,
        'days': 5,  
        'aqi': 'no',
        'alerts': 'no'
    }
    
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
       
        current_weather = data['current']
        location = data['location']['name']
        condition = current_weather['condition']['text']

        if unit == "Fahrenheit": 
            temp = current_weather['temp_f']
        else:
            temp = current_weather['temp_c']
        
        humidity = current_weather['humidity']
        wind_speed = current_weather['wind_kph']
        
        current_weather_text = (
            f"Current Weather in {location}:\n"
            f"Condition: {condition}\n"
            f"Temperature: {temp}°{unit[0]}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} km/h\n\n"
        )
        
       
        forecast_days = data['forecast']['forecastday']
        forecast_text = "5-Day Weather Forecast:\n\n"
        if unit == "Fahrenheit":
            for day in forecast_days:
                date = day['date']
                avg_temp_f = day['day']['avgtemp_f']
                forecast_condition = day['day']['condition']['text']
                max_temp = day['day']['maxtemp_f']
                min_temp = day['day']['mintemp_f']
                day_humidity = day['day']['avghumidity']
                
                forecast_text += (
                    f"Date: {date}\n"
                    f"Condition: {forecast_condition}\n"
                    f"Avg Temp: {avg_temp_f}°F\n"
                    f"Max Temp: {max_temp}°F, Min Temp: {min_temp}°F\n"
                    f"Humidity: {day_humidity}%\n\n"
                )
        else:
            for day in forecast_days:
                date = day['date']
                avg_temp_c = day['day']['avgtemp_c']
                forecast_condition = day['day']['condition']['text']
                max_temp = day['day']['maxtemp_c']
                min_temp = day['day']['mintemp_c']
                day_humidity = day['day']['avghumidity']
                
                forecast_text += (
                    f"Date: {date}\n"
                    f"Condition: {forecast_condition}\n"
                    f"Avg Temp: {avg_temp_c}°C\n"
                    f"Max Temp: {max_temp}°C, Min Temp: {min_temp}°C\n"
                    f"Humidity: {day_humidity}%\n\n"
                )

        
        return current_weather_text + forecast_text
    else:
        return None

def show_weather_and_forecast():
    city = city_entry.get()
    unit = temp_var.get()
    
    if city:
        result = get_weather_and_forecast(city,unit)
        if result:
            messagebox.showinfo("Weather and Forecast", result)
        else:
            messagebox.showerror("Error", "City not found or API request failed.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

def more_info():
    with open('D:\documents\OneDrive\Desktop\weather\Info.txt','r') as file:
        content = file.read()
        messagebox.showinfo("Info", content)

def get_location():
    
    try:
        location_response = requests.get("https://ipinfo.io")
        if location_response.status_code == 200:
            location_data = location_response.json()
            user_city = location_data['city']
            return user_city
        else:
            messagebox.showerror("Error", "Unable to fetch location. Try again later.")
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Error getting location: {e}")
        return None

def get_weather_for_current_location():
    unit = temp_var.get()
    user_city = get_location()
    if user_city:
        result1 = get_weather_and_forecast(user_city,unit)
        if result1:
            messagebox.showinfo("Forecast for current location", result1)
        else:
            messagebox.showerror("Error", "Either the city you've entered is not a valid city or the weather info for that city cannot be shown at this time")



root = tk.Tk()
root.title("Weather Forecast App")
label_frame = tk.Frame(root)

name_label = tk.Label(label_frame, text = "Name of App Author: Saurav Jayasurya" )
info_button = tk.Button(label_frame, text = "Info", command=more_info)
name_label.pack(side="left", padx=5, pady=5)
info_button.pack(side="right", padx=5, pady=5)
label_frame.pack(pady = 50)


city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

metric_label = tk.Label(root, text="Choose between temperature units")
metric_label.pack()

temp_var = tk.StringVar(value="Celsius")  
celsius_radio = tk.Radiobutton(root, text="Celsius", variable=temp_var, value="Celsius")
fahrenheit_radio = tk.Radiobutton(root, text="Fahrenheit", variable=temp_var, value="Fahrenheit")
celsius_radio.pack()
fahrenheit_radio.pack()

submit_button = tk.Button(root, text="Click here for the weather info on the city", command=show_weather_and_forecast)
submit_button.pack()

location_button = tk.Button(root, text="Get Weather for Current Location", command=get_weather_for_current_location)
location_button.pack(pady=20)


root.mainloop()
