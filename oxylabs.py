import requests

url = 'https://realtime.oxylabs.io/v1/queries'
username = 'USERNAME'
password = 'PASSWORD'
data = {
    "source": "universal",
    "url": "https://sandbox.oxylabs.io/"
}

response = requests.post(url, auth=(username, password), json=data, headers={'Content-Type': 'application/json'})

print(response.text)
