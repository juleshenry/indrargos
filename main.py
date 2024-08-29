from indrargos import Indrargos
from newsnow import NewsNowScraper
from sdb_interface import main
import asyncio


if __name__ == "__main__":
    hl_dict = Indrargos(scrapers=[NewsNowScraper()]).scrape()
    print(hl_dict)
    # asyncio.run(main(hl_dict))
