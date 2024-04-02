from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

service = Service('/path/to/chromedriver')  # Path to chromedriver executable
driver = webdriver.Chrome(service=service)
driver.get('https://www.opentable.com/nearby/restaurants-near-me-gainesville-fl')

soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find_all('h6', class_='FhfgYo4tTD0')

menu_items = [item.text.strip() for item in results]
print(menu_items)

driver.quit()