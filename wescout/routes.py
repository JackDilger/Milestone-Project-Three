from flask import render_template
from wescout import app, db
from wescout.models import Region, Player

@app.route("/")
def home():
    return render_template("tasks.html")

