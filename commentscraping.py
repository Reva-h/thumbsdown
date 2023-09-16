import requests
from bs4 import BeautifulSoup as bs

def get_site(site_url = ""):
    """
    Get the json content of given site using requests library
    Returns content object of site to be injested into BS
    """
    try:
        page = requests.get(site_url)
        #print(page.status_code)
        #print(page.content)
        return page.content

    except Exception as e:
        #Requests failed
        print(e)
    


def get_youtube_comments(request_content):
    """
    Use Soup with the requests object to parse through youtube comments section
    Return list of dict of youtube comments: {username: [comments]}
    """
    # soup = bs(request_content, "html.parser")
    soup = bs(request_content, "html5lib")
    # comment_list = soup.findAll('tr', attrs = {class : 'commtext c00'})
    comment_list = soup.find_all(class_='commtext c00')
    #newlist = comment_list.split("commtext c00\">")
    print(comment_list)


def main():
    result = get_site('https://news.ycombinator.com/item?id=37534615')
    get_youtube_comments(result)

if __name__ == "__main__":
    main()



