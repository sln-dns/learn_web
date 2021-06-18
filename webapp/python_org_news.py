import requests
from bs4 import BeautifulSoup

def get_html(url):
    try: 
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False

def get_python_news():
        html = get_html("https://www.python.org/")
        if html:
            soup = BeautifulSoup(html, "html.parser")
            all_news = soup.find("div", class_ = "blog-widget")
            all_news = all_news.find("ul", class_ = "menu")
            all_news = all_news.findAll('li')
            result_news = []
            for news in all_news:
                title = news.find('a').text
                url = news.find('a')['href']
                published = news.find('time').text
                result_news.append({
                    "title": title,
                    "url": url,
                    "published": published

                })
            return result_news
        return False

