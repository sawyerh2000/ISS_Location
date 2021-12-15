# ISS_Location
Flask app to retrieve data on the location of the ISS using open-notify API and use it to retrieve weather data pertaining to that area using openweathermap API.

In order to run on local machine, a config.py file will need to be made in the root project directory with the following format:

#######
space_key = "YOUR_API_KEY" #from https://positionstack.com/

weather_key = "YOUR_API_KEY" #from https://openweathermap.org/api
#######

This project is fairly basic, but I'm using it as an introduction to the fundamentals of API's. I'm using both empty calls and parametized calls to gain familiarity with both, 
and in the future I'd like to update the fairly simple stack of this project to include javascript libraries such as jquery with AJAX to update data asychronously without the need 
to refresh the page to obtain said data. Frontend certainly isn't my favorite, but I'd also like to incorporate more CSS and JS into the frontend to beautify it just a bit. 
