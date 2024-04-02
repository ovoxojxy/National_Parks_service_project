import requests
from bs4 import BeautifulSoup

URL = 'https://www.opentable.com/nearby/restaurants-near-me-gainesville-fl'

headers = {'User-Agent' : 'Mozilla/5.0'}

try:
    page = requests.get(URL, headers=headers, timeout=100)
except requests.RequestException as e:
    print('Error fethcing page:', e)
    exit()

if page.status_code != 200:
    print("failed to fetch page:", page.status_code)
    exit()

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all( 'h6', class_ = 'FhfgYo4tTD0')

menu_items = []

print(results)

