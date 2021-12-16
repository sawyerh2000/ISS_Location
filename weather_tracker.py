import requests
import Space_Tracker
import json
import config
API_KEY = config.weather_key



def weather(): 



    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + Space_Tracker.getLat() + "&lon=" + Space_Tracker.getLong() + "&units=imperial"+ "&appid=" + API_KEY

    conn = requests.get(url)

    str1 = json.dumps(conn.json(), indent=4, sort_keys=True)

    dict1 = json.loads(str1)

    return dict1



def getCondition(weatherDict):
    temperature = str(weatherDict['main']['temp'])
    conditions = weatherDict['weather'][0]['description']
    windspeed = str(weatherDict['wind']['speed'])

    str1="The temperature is "+ temperature +", the current conditions are "+ conditions +", and the windspeed is " + windspeed + " mph."

    return str1














