from flask import Flask, render_template, request, url_for
import Space_Tracker
import weather_tracker

app=Flask(__name__)

@app.route("/location") 
def location():
     s = Space_Tracker.iss_location()
     w = Space_Tracker.world_location()
     weather = weather_tracker.getCondition(weather_tracker.weather())
     return render_template('location.html', loc=s, world=w, track = weather)


if __name__ == "__main__":
    app.run(debug=True) 