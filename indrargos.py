from newsnow import NewsNowScraper
from motor import MotorMonoFunction
import json

class Indrargos:

    def __init__(self, scrapers):
        self.scrapers = None
        self.__validate_scrapers(scrapers)
        with open("edition.json", "r") as f:
            self.edition = json.loads(f.read())['current']
        print(self.edition)

    def __validate_scrapers(self, scrapers):
        for scraper in scrapers:
            if not hasattr(scraper, "get_headlines"):
                raise Exception(f"Scraper {scraper} does not have get_headlines method")
            if not hasattr(scraper, "get_urls"):
                raise Exception(f"Scraper {scraper} does not have get_urls method")
        self.scrapers = scrapers

    def scrape(self):
        headlines = []
        for scraper in self.scrapers:
            headlines += MotorMonoFunction(function=scraper.get_headlines).multithread_function(
                    [
                        (
                            scraper.make_driver(),
                            url,
                        )
                        for url in scraper.get_urls()
                    ]
                )
            
        return headlines

if __name__=='__main__':
    Indrargos([NewsNowScraper])