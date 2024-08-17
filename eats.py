from selenium import webdriver
from selenium.webdriver.chrome.options import Options

newsnow_urls = [
    "https://www.newsnow.com/us/World/Latin+America/South+America",
    "https://www.newsnow.com/us/World/Europe",
    "https://www.newsnow.com/us/World/Asia",
    "https://www.newsnow.com/us/World/Africa",
    "https://www.newsnow.com/us/World/Caribbean",
    "https://www.newsnow.com/us/World/Middle+East",
    "https://www.newsnow.com/us/World/South+Pacific"
    "https://www.newsnow.com/us/World/Latin+America/Central+America",
]

def ingest_url(url):
    '''
    Ingests newsnow urls for each region
    html class is class="article-title top-title list-layout"
    '''
    
ingest_url(newsnow_urls[0])