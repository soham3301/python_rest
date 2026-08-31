
from flask import Flask

app = Flask(__name__)

def make_bold(the_func):
    def wrapper_func():
        return f"<b>{the_func()}</b>"
    return wrapper_func

def make_italic(the_func):
    def wrapper_func():
        return f"<em>{the_func()}</em>"
    return wrapper_func

def make_underline(the_func):
    def wrapper_func():
        return f"<u>{the_func()}</u>"
    return wrapper_func

@app.route("/")
@make_bold
@make_italic
@make_underline
def index_page():
    return "This is our Index Page"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}, Have a good day"

@app.route("/explorepath/<path:anything>")
def with_path(anything):
    return f"{anything}"

@app.route("/<int:got_int>")
def print_the_int(got_int):
    return f"Got this number: {got_int}"

@app.route("/testhtml")
def proper_html():
    return '<h1 style="text-align: center">This is the Heading</h1>' \
    '<p>This is the Paragraph</p>' \
    '<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdThmaHc2cW8wZDRrMHA2Nnptcmk0OGR0c2J0cmwxdTk2YzdieGN4ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/goZDkNssE24sWUiAiO/giphy.gif>' \
    '<h3>This is the ending</h3>'

if __name__ == "__main__":
    app.run(debug=True)