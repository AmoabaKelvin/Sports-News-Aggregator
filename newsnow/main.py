import concurrent.futures

import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    """
    This function gets the html from the url and returns it.
    """
    response = requests.get(url)
    return response.text


def get_news():
    """
    This function gets the news from the url and returns it.
    """
    html = get_html(
        "https://www.newsnow.co.uk/h/Sport/Football/Premier+League/Tottenham+Hotspur"
    )
    soup = BeautifulSoup(html, "html.parser")
    news = soup.find_all("div", class_="rs-newsbox")[1]
    newsfeed = news.find_all("div", class_="hl")
    return newsfeed


def get_news_heading() -> list:
    """
    This function gets the news heading from the url and returns it.
    """
    news = get_news()
    heading = [i.text for i in news]
    return heading


def open_news_link() -> list:
    """
    This function gets the news link from the news ResultQuery and returns it.
    """
    news = get_news()
    links = [i.a.get("href") for i in news]
    return links


def fetch() -> tuple[list, list]:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        set1 = executor.submit(get_news_heading)
        set2 = executor.submit(open_news_link)

        headings = list(map(lambda x: x.strip(), set1.result()))
        links = set2.result()
    return headings, links


# if __name__ == "__main__":
#     headings, links = fetch()
#     for i, v in zip(headings, links):
#         print(f"{i} - {v}")
