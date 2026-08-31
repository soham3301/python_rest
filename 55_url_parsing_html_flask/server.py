
from flask import Flask
import random

app = Flask(__name__)

generated_random_number = random.randint(1, 9)
print(generated_random_number)


@app.route("/")
def index_page():
    return f'<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'

@app.route("/<int:value>")
def another_page(value):
    if value < generated_random_number:
        return f'<h1>Too Low, Try Again</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
    elif value > generated_random_number:
        return f'<h1>Too High, Try Again</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        return f'<h1>You Got It Correctly</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'

if __name__ == "__main__":
    app.run(debug=True)