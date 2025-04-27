from flask import Flask, render_template, request
import bd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/forgot-password")
def forgot_password():
    return "<h1>Страница восстановления пароля (в разработке)</h1>"




@app.route("/enter", methods = ["POST"])
def enter():
    username = request.form["username"]
    password = request.form["password"]
    result = bd.enter(username, password)
    if result:
        return "OK"
    else:
        return "NE OK"


if __name__ == "__main__":
    app.run(debug=True)