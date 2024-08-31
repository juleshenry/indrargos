# Practical news getting scraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime


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
        return webdriver.Chrome(
            service=Service("./cd/chromedriver"), options=chrome_options
        )

    @staticmethod
    def get_headlines(driver, url):
        driver.get(url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/16);")
        time.sleep(5)
        headlines = []
        try:
            elements = driver.find_elements(By.CLASS_NAME, "hll")
            print("Headlines found: ", len(elements))
            if not len(elements):
                raise Exception("No elements found")
            for element in elements:
                if not getattr(element, "text", 0) or not element.text.strip():
                    continue
                headlines.append(
                    rf"{element if type(element) == str else element.text}"
                )
        except Exception as e:
            print("!!!", e)
        driver.quit()
        country = url.split("/")[-1].split("?")[0].replace("+", " ")
        return [{
            "country": country,
            "headline": h,
            "edition": 1
        } for h in headlines]

    @staticmethod
    def get_urls(latest=True):
        latest = "?type=ln" if latest else ""
        newsnow_urls = [
            "https://www.newsnow.com/us/World/Latin+America/South+America",
            "https://www.newsnow.com/us/World/Europe",
            "https://www.newsnow.com/us/World/Africa",
            "https://www.newsnow.com/us/World/Caribbean",
            "https://www.newsnow.com/us/World/Middle+East",
            "https://www.newsnow.com/us/World/South+Pacific"
            "https://www.newsnow.com/us/World/Latin+America/Central+America",
            "https://www.newsnow.com/us/World/North+America",
        ]
        newsnow_urls = [newsnow_urls[0]]
        return [nnu + latest for nnu in newsnow_urls]


if __name__ == "__main__":
    for url in NewsNowScraper.get_urls():
        hhh = NewsNowScraper.get_headlines(url)

    # print(*['[']+[f'"{x}",' for x in o.split('\n') if x.strip()]+[']'],sep='\n')
