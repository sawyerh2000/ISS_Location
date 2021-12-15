import requests
import Space_Tracker
import json
import config
API_KEY = config.weather_key



def weather(): 
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + Space_Tracker.getLat() + '&lon=' + Space_Tracker.getLong() + '&appid='+API_KEY

    conn = requests.get(url)

    str1 = json.dumps(conn.json(), indent=4, sort_keys=True)

    dict1 = json.loads(str1)

    print(dict1)


print(Space_Tracker.world_location())
weather()








