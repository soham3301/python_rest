from flask import Flask
app = Flask(__name__)


def my_site():
    return "Hey this is Soham's first python site"

@app.route('/')
def hello_world():
    return my_site()

@app.route("/bye")
def goodbye():
    return "Bye Bye"

if __name__ == "__main__":
    app.run()

#? Testing github connection