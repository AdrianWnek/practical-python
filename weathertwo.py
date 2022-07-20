import requests

def get_weather_desc_and_temp():
    api_key = "bc12083e70d2d22298c2df1cec7101d9"
    city = "Orlando"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()
    print(json)

    desctiption = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': desctiption,
            'temp_min': temp_min,
            'temp_max': temp_max}
def main():
    # Print the results
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is", weather_dict.get('desctiption'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

main()    