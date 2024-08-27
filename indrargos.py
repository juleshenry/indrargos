from newsnow import NewsNowScraper


class Partial:
    def __init__(self, func, arg):
        self.func, self.arg = func, arg

    def __call__(self):
        self.func(self.arg)


class Indrargos:

    def __init__(self, scrapers):
        self.__validate_scrapers(scrapers)
        self.scrape_funcs = []
        self.__assemble_functors(scrapers)

    def __validate_scrapers(self, scrapers):
        for scraper in scrapers:
            if not hasattr(scraper, "get_headlines"):
                raise Exception(f"Scraper {scraper} does not have get_headlines method")
            if not hasattr(scraper, "get_urls"):
                raise Exception(f"Scraper {scraper} does not have get_urls method")

    def __assemble_functors(self, scrapers):
        for scraper in scrapers:
            for url in scraper.get_urls():
                self.scrape_funcs += [lambda: Partial(scraper.get_headlines, url)]

    def scrape(self):
        for functor in self.functors:
            functor()


if __name__ == "__main__":
    Indrargos(scrapers=[NewsNowScraper()])
