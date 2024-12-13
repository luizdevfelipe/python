from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ("Basketball", "Football", "Soccer", "Running")

@app.route("/", methods=["GET"])
def index():        
    return render_template("index.html", sports=SPORTS)

@app.route("/sport", methods=["POST"])
def sport():
    if not request.form.get("name"):
        return render_template("error.html", error="Invalid Values")
    for sport in request.form.getlist("sport"):
        if sport not in SPORTS:
            return render_template("error.html", error="Invalid Values")
        
    sport = request.form.getlist("sport")
    name = request.form.get("name")
    return render_template("sport.html", sports=sport, name=name)