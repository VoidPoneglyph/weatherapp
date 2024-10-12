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
        
        weather_description = current['condition']['text']  
        temp = current['temp_c']  
        humidity = current['humidity']  
        wind_speed = current['wind_kph']  

        return {
            'Location': location['name'],
            'Temperature': temp,
            'Humidity': humidity,
            'Description': weather_description,
            'Wind Speed': wind_speed
        }
    else:
        return None

def main():
    api_key = 'fe5ece531c06400aa58112348240910'  
    city_name = input("Enter the name of the city: ")
    metric_of_temp = input("Type C for Celcius or F for Farenheit: ")
    weather_data = get_weather(city_name, api_key)
    
    if weather_data:
        print(f"Weather in {weather_data['Location']}:")
        if metric_of_temp == "C":
            print(f"Temperature: {weather_data['Temperature']}°C")
        if metric_of_temp == "F":
            print(f"Temperature:{(weather_data['Temperature']*1.8) + 32}°F")
            
        print(f"Humidity: {weather_data['Humidity']}%")
        print(f"Status: {weather_data['Description']}")
        print(f"Wind Speed: {weather_data['Wind Speed']} km/h")
    else:
        print("Either you've entered an invalid city name or the request didn't go through.")
   
if __name__ == "__main__":
    main()