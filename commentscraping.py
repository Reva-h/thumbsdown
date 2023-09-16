import requests
from bs4 import BeautifulSoup as bs

def get_site(site_url = ""):
    """
    Get the json content of given site using requests library
    Returns content object of site to be injested into BS
    """
    try:
        page = requests.get(site_url)
    except Exception as e:
        #Requests failed
        print(e)

    return page.content

<<<<<<< HEAD

#def get_youtube_comments()
    """
    Use Soup with the requests object to parse through youtube comments section
    Return list of dict of youtube comments: {username: [comments]}
    """

def main():
    get_site("https://discord.com/channels/@me/1152469841937190984/1152680543482286191")


if __name___ == "__main__":
    main()
=======
def get_youtube_comments():
    ''' get input from user or frontend or something idk'''

    soup = bs(get_site('https://www.youtube.com/watch?v=t0X0gLEsAfI&ab_channel=HashtagUnited'), "html.parser")
    results = soup.find(id = 'content-text')
    print(results)

"""
Use Soup with the requests object to parse through youtube comments section
Return list of dict of youtube comments: {username: [comments]}
"""

get_youtube_comments()
>>>>>>> refs/remotes/origin/scraping
