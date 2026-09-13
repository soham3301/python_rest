
from flask import Flask, render_template, abort, request

app = Flask(__name__)

the_username = "soham3301"
the_password = "12345"

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login_checker():
    if request.method == "POST":
        username = request.form["uname"]
        password = request.form["pwd"]
        if username == the_username and password == the_password:
            return render_template('logged_in.html')
        else:
            return render_template('login_failed.html')
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)