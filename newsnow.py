# Practical news getting scraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class NewsNowScraper:
    """
    Scrapes headlines from newsnow.com

    learned by inspecting requests. Found out inspector differs from raw request

    >>>
    import requests
    url = "https://www.newsnow.com/us/World/Latin+America/South+America?type=ln"
    response = requests.get(url)
    with open('newsnow.html', 'w') as f:
        f.write(response.text)
    >>>
    
    """
    
    @staticmethod
    def make_driver():
        chrome_options = Options()
        chrome_options.add_argument("--user-agent=Your Custom User-Agent String")
        return webdriver.Chrome(service=Service('./cd/chromedriver'), options=chrome_options)

    @staticmethod
    def get_headlines(driver, url):
        driver.get(url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/16);")
        time.sleep(5)
        headlines = []
        try:
            headlines = driver.find_elements(By.CLASS_NAME, 'hll')
            print("Headlines found: ", len(headlines))
            if not len(headlines):
                raise Exception("No elements found")
            for o in headlines:
                if not getattr(o,'text', 0) or not o.text.strip():
                    continue
                headlines.append(rf'{o if type(o) == str else o.text}')
        except Exception as e:
            print('!!!',e)
        driver.quit()
        return headlines

    @staticmethod
    def get_urls(latest=False):
        latest = "?type=ln" if latest else ""
        # TODO: add more urls
        newsnow_urls = [
            "https://www.newsnow.com/us/World/Latin+America/South+America",
            "https://www.newsnow.com/us/World/Europe",
            "https://www.newsnow.com/us/World/Africa",
            "https://www.newsnow.com/us/World/Caribbean",
            "https://www.newsnow.com/us/World/Middle+East",
            "https://www.newsnow.com/us/World/South+Pacific"
            "https://www.newsnow.com/us/World/Latin+America/Central+America",
        ]
        newsnow_urls = ["https://www.newsnow.com/us/World/Asia/Mongolia"]
        return [nnu+latest for nnu in newsnow_urls]


if __name__=='__main__':
    for url in  NewsNowScraper.get_urls():
        hhh = NewsNowScraper.get_headlines(NewsNowScraper.make_driver(),url)
        print(*hhh,sep='\n')

    
    # print(*['[']+[f'"{x}",' for x in o.split('\n') if x.strip()]+[']'],sep='\n')