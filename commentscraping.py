import requests
from bs4 import BeautifulSoup as bs

url = "https://www.youtube.com/watch?v=t0X0gLEsAfI&ab_channel=HashtagUnited"
page = requests.get(url)

soup = bs(page.content, "html.parser")


def get_site()
"""
Get the json content of given site using requests library
Returns request object of site
"""

def get_youtube_comments()
"""
Use Soup with the requests object to parse through youtube comments section
Return list of dict of youtube comments: {username: [comments]}
"""