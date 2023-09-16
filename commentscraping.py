import requests
from bs4 import BeautifulSoup as bs

def get_site(site_url = ""):
    """
    Get the json content of given site using requests library
    Returns content object of site to be injested into BS
    """
    try:
        page = requests.get(site_url)
        print(page.status_code)
        return page.content

    except Exception as e:
        #Requests failed
        print(e)
    


def get_youtube_comments():
    """
    Use Soup with the requests object to parse through youtube comments section
    Return list of dict of youtube comments: {username: [comments]}
    """

    soup = bs(get_site('https://www.youtube.com/watch?v=t0X0gLEsAfI&ab_channel=HashtagUnited'), "html.parser")
    results = soup.find(id = 'content-text')
    print(results)


def main():
    get_site('https://www.youtube.com/watch?v=t0X0gLEsAfI&ab_channel=HashtagUnited')

    get_youtube_comments()


if __name__ == "__main__":
    main()



