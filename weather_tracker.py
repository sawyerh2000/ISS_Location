import requests
import Space_Tracker
import json
import config
API_KEY = config.weather_key



def weather(): 
    param = {
    "lat" :  Space_Tracker.getLat(),
    "long" : Space_Tracker.getLong(),
    "API_Key" : API_KEY
}

    conn = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_Key}", params=param)

    str1 = json.dumps(conn.json(), indent=4, sort_keys=True)

    dict1 = json.loads(str1)

    print(dict1)

weather()








