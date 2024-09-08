from indrargos import Indrargos
from newsnow import NewsNowScraper
from sdb_interface import insert_data, query_data, delete_data
import asyncio
import sys


def shell_main():
    print("Calling Indrargos with edition: ", sys.argv[1])
    # Uncomment when in production
    main(edition=sys.argv[1])

def main(edition=""):
    # asyncio.run(delete_data()) # as needed to clear the database
    hl_dict = Indrargos(scrapers=[NewsNowScraper()]).scrape()
    hl_dict = [{"headline": h["headline"], "country": h["country"], "edition": int(edition)} for h in hl_dict]
    asyncio.run(insert_data(hl_dict))
    # asyncio.run(query_data())

if __name__ == "__main__":
    shell_main()
