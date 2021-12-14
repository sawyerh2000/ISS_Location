from flask import Flask, render_template, request, url_for
import Space_Tracker

app=Flask(__name__)

@app.route("/location") 
def location():
     s = Space_Tracker.iss_location()
     w = Space_Tracker.world_location()
     return render_template('location.html', loc=s, world=w)


if __name__ == "__main__":
    app.run(debug=True) 