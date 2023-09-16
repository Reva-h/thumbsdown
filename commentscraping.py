import requests
from bs4 import BeautifulSoup as bs

soup = bs(page.content, "html.parser")

def get_site(site_url = ""):
    """
    Get the json content of given site using requests library
    Returns content object of site to be injested into BS
    """
    try:
        page = requests.get(url)
    except Exception as e:
        #Requests failed
        print(e)

    return page.content


#def get_youtube_comments()
    """
    Use Soup with the requests object to parse through youtube comments section
    Return list of dict of youtube comments: {username: [comments]}
    """

def main():
    get_site("https://discord.com/channels/@me/1152469841937190984/1152680543482286191")


if __name___ == "__main__":
    main()