import requests
import datetime 
import json
import http.client, urllib.parse
import config


ACCESS_KEY = config.space_key

#Function to get the number and data of astronauts currently in space 
def get_astros():
    json_response = requests.get('http://api.open-notify.org/astros.json') #send GET request to api endpoint contain json data on current astronauts in space

    str_result = json.dumps(json_response.json(), sort_keys= True, indent= 4) #Format JSON from GET request into a string 

    dict1 = json.loads(str_result) #load string into a python dictionary

    print(dict1['number']) #print number of astronauts in space currently


#Function to get location of ISS in latitude and longitude 
def iss_location(): 
    json_response = requests.get('http://api.open-notify.org/iss-now.json') #send GET request to endpoint 

    str_res = json.dumps(json_response.json(), indent=4, sort_keys=True) #represent json data as string

    dict1 = json.loads(str_res) #load string into dictionary object

    str1=dict1['iss_position']['latitude'] + ',' + dict1['iss_position']['longitude'] #place latitude and longitude from dict into string

    return str1 #return string


#Function to use coordinates from iss_location() to give more readable format of ISS location. 
def country(coords):

    conn = http.client.HTTPConnection('api.positionstack.com')  #connect to server

    params = urllib.parse.urlencode({         #encode url parameters (api key and coords)
        'access_key' : ACCESS_KEY,
        'query' : coords
    })

    conn.request('GET', '/v1/reverse?{}'.format(params)) #GET request to endpoint on server
    res = conn.getresponse() #reponse from endpoint (json data)
    data = res.read()  #reads data 
    dict1 = json.loads(data.decode('utf-8')) #decode data into readable format and load into dict and print data key from dict
    try:
        str1 = dict1['data'][0]['name'] + ', ' + str(dict1['data'][0]['country'])
        return str1 
    except:
        return "Unavailable, server failed to respond."
 
def world_location():
    return country(iss_location())

def coords(coords):
    return coords.split(",")

def getLat():
    return coords(iss_location())[0]

def getLong():
    return coords(iss_location())[1]





    