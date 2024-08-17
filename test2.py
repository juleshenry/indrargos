import requests
from bs4 import BeautifulSoup
import time
url = "https://www.newsnow.com/us/World/Latin+America/South+America?type=ln"

response = requests.get(url)
# response = requests.get(url, headers=headers).json()
with open('newsnow.html', 'w') as f:
    f.write(response.text)
# print(response.content)
# soup = BeautifulSoup(response.content, "html.parser")
# time.sleep(5)  # Wait for 5 seconds

# spans = soup.find_all("span")
# for span in spans:
#     print(span.text)