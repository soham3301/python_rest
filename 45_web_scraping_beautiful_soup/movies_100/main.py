import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
result = response.text

soup = BeautifulSoup(result, "html.parser")

titles = soup.find_all(name="h3")

movie_data = {}

for title in reversed(titles):
    movie_serials = title.getText().split(" ")[0]
    movie_names = " ".join(title.getText().split(" ")[1:])
    movie_data[movie_serials] = movie_names

with open("./movies.txt", mode="a") as file:
    for data in movie_data:
        file.write(f"{data} {movie_data[data]}\n")