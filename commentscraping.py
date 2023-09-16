import requests
from bs4 import BeautifulSoup as bs

url = "https://www.youtube.com/watch?v=t0X0gLEsAfI&ab_channel=HashtagUnited"
page = requests.get(url)

soup = bs(page.content, "html.parser")


print("Tets")