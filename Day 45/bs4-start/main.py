from bs4 import BeautifulSoup
import lxml


with open("website.html", 'r', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")

print(soup)  # get the whole web page.
print(soup.prettify()) # get whole webpage with indentation.
print(soup.title)  # to get title tag with content from the webpage. We can use other HTML tags.
print(soup.title.name)  # just get the tag name.
print(soup.title.string)  # just for content of inside title tag.
print(soup.a)  # it will print the 1st anchor(a) tag of this page.
print(soup.find_all(name="a"))  # this will show all the anchor tags in a python list.
print(soup.find_all(name="img"))  # show all the image tags in a python list.

all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    # this one will show the texts of all the anchor tags.
    print(tag.getText())

for tag in all_anchor_tags:
    # to get all the link of anchor tags.
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")  # get any particular element with tag name and id.
print(heading)  # it will print the whole thing tag and content.
print(heading.getText())  # get just the text of an element.

name = soup.select_one(selector="#name")

