from flask import Flask, render_template, request
import bd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enter", methods = ["POST"])
def enter():
    login = request.form["username"]
    password = request.form["password"]
    result = bd.enter(username, password)
    if result:
        return "OK"
    else:
        return "NE OK"


app.run()