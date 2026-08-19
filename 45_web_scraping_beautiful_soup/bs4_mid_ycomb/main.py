
import json
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# first_article_text = soup.find(class_="titleline").getText()

# print(first_article_text)

all_article_texts = soup.find_all(class_="titleline")
article_scores = soup.find_all(class_="score")

headlines = {}
for text in all_article_texts:
    headline = text.getText()
    url = text.select_one(selector="a").get("href")
    headlines[headline] = {
        "url": url,
        "upvote": 0
    }

upvotes = []

for score in article_scores:
    the_score = int(score.getText().split(" ")[0])
    upvotes.append(the_score)

# print(upvotes)

counter = 0

for key, value in headlines.items():
    value["upvote"] = upvotes[counter]
    counter += 1

# print(headlines)

# with open("./test_json", mode="w") as write_file:
#     json.dump(headlines, write_file, indent=4)

highest_upvote = 0
for item_headline, item_details in headlines.items():
    if item_details["upvote"] > highest_upvote:
        highest_upvote = item_details["upvote"]

for head_key, head_value in headlines.items():
    if head_value["upvote"] == highest_upvote:
        print(f"Headline: {head_key} | Link: {head_value["url"]}")
