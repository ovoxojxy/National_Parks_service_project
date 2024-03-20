import requests
from bs4 import BeautifulSoup

URL = 'https://www.visitgainesville.com/dine/'

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

results = soup.find_all(class_='card-content tcenter')

restaurants = []

for result in results:
    restaurant = result.find('h3')
    if restaurant:
        restaurants.append(restaurant.text.strip())

if restaurants:
    for idx, restaurant_name in enumerate(restaurants, start=1):
        print(f"{idx}. {restaurant_name}")
else:
    print('No results found')


#restaurant = results.find_all('h3')



#if results is not None:

#    print(restaurant)
    
#else:
#    print("No results found.")


