
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)



@app.route("/")
def home():
    year = datetime.date.today().year
    random_number = random.randint(1, 9)
    return render_template("index.html", ran_num = random_number, the_year = year)

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get("https://api.genderize.io", params={"name": name})
    gender_result = gender_response.json()
    age_response = requests.get("https://api.agify.io", params={"name": name})
    age_result = age_response.json()
    return render_template("guess.html", username = gender_result["name"].title(), gender = gender_result["gender"], age = age_result["age"])

@app.route("/blog/<number>")
def get_blog(number):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(url=url)
    blog_result = blog_response.json()
    print(number)
    return render_template("blog.html", post = blog_result)


if __name__ == "__main__":
    app.run(debug=True)