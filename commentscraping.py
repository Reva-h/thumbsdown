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
    # comment_list = soup.findAll(class_="commtext c00", text=lambda s: "Fiscal" in s and "year" not in s)
    comment_list = soup.find_all(class_='commtext c00')
    #newlist = comment_list.split("commtext c00\">")
    print(str(comment_list[0].text)[0:-5] + '\n--------------------------------------\n' +
            str(comment_list[1].text)[0:-5] + '\n--------------------------------------\n' +
            str(comment_list[2].text)[0:-5] + '\n--------------------------------------\n' +
            comment_list[3].text + '\n--------------------------------------\n'
        )


def main():
    result = get_site('https://news.ycombinator.com/item?id=37534615')
    get_youtube_comments(result)

if __name__ == "__main__":
    main()



