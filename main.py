from flask import Flask, render_template, request, redirect, url_for
import bd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/forgot-password")
def forgot_password():
    return "<h1>Страница восстановления пароля (в разработке)</h1>"

@app.route("/enter", methods=["POST"])
def enter():
    username = request.form["username"]
    password = request.form["password"]
    result = bd.enter(username, password)
    if result:
        return redirect(url_for("main"))
    else:
        # Передаем ошибку и сохраненные значения обратно в шаблон
        return render_template("index.html", 
                            login_error="Неверный логин или пароль",
                            saved_username=username)

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]

    result = bd.add_user(username, (username, password))

    if result:
        return redirect(url_for("main"))
    else: 
        return "no"


@app.route("/main", methods = ["POST", "GET"])
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)



