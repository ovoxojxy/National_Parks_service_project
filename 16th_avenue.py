import requests
from bs4 import BeautifulSoup

URL = 'https://16th-avenuediner.com/menu/'

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

results = soup.find_all( class_ = 'woofoo-title')

menu_items = []

print(results)

# for result in results:
#     menu_item = result.find('h2')
#     if menu_item:
#         menu_items.append(menu_item.text.strip())

# if menu_items:
#     for idx, menu_itm in enumerate(menu_items, start = 1):
#         print(f'{idx}. {menu_itm}')
# else:
#     print('No results found')

#if results is not None:
#    print(results.prettify())
#else:
#    print("No results found.")