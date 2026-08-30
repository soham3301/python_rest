
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/gp/product/B0F48FQS68/ref=ox_sc_saved_title_4?th=1"

response = requests.get(URL)

result = response.text

soup = BeautifulSoup(result, "html.parser")

print(soup.prettify())