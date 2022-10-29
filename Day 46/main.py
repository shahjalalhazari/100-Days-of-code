from bs4 import BeautifulSoup
import requests
import lxml

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n>>> ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
movies_list = response.text

soup = BeautifulSoup(movies_list, "lxml")

song_name = soup.select_one(selector="#title-of-a-story")
# print(song_name)
print(song_name.getText())