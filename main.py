from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time


GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSekxe5KCVAL0W-7pSdiwl1i3OiGDMelIPbXsmWD6PDDag1KmA/viewform?usp=sf_link'
zillow = 'https://www.zillow.com/jersey-city-nj/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Jersey%20City%2C%20NJ%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.1979920168457%2C%22east%22%3A-73.9394699831543%2C%22south%22%3A40.60900960866344%2C%22north%22%3A40.82135326481596%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A25320%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22price%22%3A%7B%22max%22%3A400179%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.9',
}

response = requests.get(zillow, headers=HEADERS)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

href_list = []
address_list = []
price_list = []
listings = soup.select('li article')

for listing in listings:

    try:
        href_data = listing.find('a', class_='StyledPropertyCardDataArea-c11n-8-82-3__sc-yipmu-0 hiBOYq property-card-link')['href']
        if href_data.startswith('https://'):
            href_list.append(href_data)
        else:
            href_list.append(f'https://www.zilliw.com{href_data}')
        address = listing.find('a', class_='StyledPropertyCardDataArea-c11n-8-82-3__sc-yipmu-0 hiBOYq property-card-link').text
        address_list.append(address)

        price_data = listing.find('div', class_='StyledPropertyCardDataArea-c11n-8-82-3__sc-yipmu-0 gMDnGj').text
        if '+' in price_data:
            price_list.append(price_data.split('+')[0])
        elif '/' in price_data:
            price_list.append(price_data.split('/')[0])

    except TypeError:
        continue
    except AttributeError:
        continue


CHROME_DRIVER_PATH = r'C:\Users\*********\OneDrive\Desktop\python\chromedriver.exe'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(GOOGLE_FORM_URL)

for i in range(len(href_list)):
    time.sleep(1)
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address_list[i])
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price_list[i])
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(href_list[i])
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(3)
    test = driver.find_element(By.LINK_TEXT, value='Submit another response')
    test.click()

driver.close()

