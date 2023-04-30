import requests

api_key = "620a21a709418f0e9d81500fde3a1078"  # My API key from OpenWeatherMap


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Convert temperature from Kelvin to Celsius and round off to 1 decimal place
        temp = round(data["main"]["temp"] - 273.15, 1)
        desc = data["weather"][0]["description"]
        return f"The current temperature in {city} is {temp}°C and the weather is {desc}."
    else:
        return "Sorry, I couldn't retrieve the weather information for that location."


print("Hi! I'm a Weather Bot. Please enter the name of a city to get its current weather conditions.")
while True:
    city = input("City: ")
    if city.lower() == "quit":
        break
    print(get_weather(city))
