
import requests
from bs4 import BeautifulSoup

response = requests.get("https://joyb.works/")
joy_page = response.text

joy_soup = BeautifulSoup(joy_page, "html.parser")

print(joy_soup.prettify())