from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "lxml")
print(soup.title)

all_titles = soup.find_all(name="a", class_="titlelink")
for title in all_titles:
    title = title.getText()
    print(title)
    link = title.get("href")
    print(link)

