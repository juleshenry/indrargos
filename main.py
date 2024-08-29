from indrargos import Indrargos
from newsnow import NewsNowScraper
from sdb_interface import insert_data, query_data, delete_data
import asyncio


if __name__ == "__main__":
    # hl_dict = Indrargos(scrapers=[NewsNowScraper()]).scrape()
    # asyncio.run(delete_data())
    # print(hl_dict)
    # asyncio.run(insert_data(hl_dict))
    asyncio.run(query_data())