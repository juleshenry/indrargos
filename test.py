import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#CLASS_NAME', 'CSS_SELECTOR', 'ID', 'LINK_TEXT', 'NAME', 'PARTIAL_LINK_TEXT', 'TAG_NAME', 'XPATH'
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--user-agent=Your Custom User-Agent String")
service = Service('./cd/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.newsnow.com/us/World/Latin+America/South+America?type=ln")
# time.sleep(4)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/6);")
#.article-title.top-title.list-layout')
# /html/body/div[2]/div[2]/div/div/div/div[1]/section/div[1]/div[2]/article/div/div/span/a/span
#/html/body/div[2]/div[2]/div/div/div/div[1]/section/div[1]/div[2]/article/div/div/span/a/span
time.sleep(5)
try:
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    # Wait for the element to be located
    # wait = WebDriverWait(driver, 10)
    # es = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/section/div[1]/div[2]/article/div/div/span/a/span')))
    es = driver.find_elements(By.CLASS_NAME, 'hll')
    print(es)
    if not len(es):
        raise Exception("No elements found")
    for o in filter(lambda x:x.text.strip(),es):
        print(rf'{o.text}')
except Exception as e:
    print(e)

# element = driver.find_element(By.TAG, 'article-title top-title') 

# Close the browser
driver.quit()