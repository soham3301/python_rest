
from bs4 import BeautifulSoup
import lxml

with open("./website.html") as file:
    render_html = file.read()
    # print(render_html)

# with open("./website.txt", mode="w") as another_file:
#     for row in render_html:
#         another_file.write(row)

soup = BeautifulSoup(render_html, "html.parser")

soup.title #? The title
soup.body #? The body

all_paragraphs = soup.find_all(name="p")    #? returns all <p> tags inside a list
all_anchor_tags = soup.find_all(name="a")   #? returns all <a> tags inside a list

for tag in all_anchor_tags:
    print(tag.getText())                    #? returns all texts inside a tag
    print(tag.get("href"))                  #? returns all the links inside a tag

heading = soup.find(name="h1", id="name")   #? getting the 1h using id
print(heading)

h3 = soup.find(name="h3", class_="heading") #? getting the h3 using class
print(h3)
print(h3.get("class"))                      #? getting the value of the attribute

company_url = soup.select_one(selector="p a")   #? getting a perticular tag using css selectors [here <a> tag is inside a <p> tag in the html file]
print(company_url)
