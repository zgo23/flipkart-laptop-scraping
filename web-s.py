from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from extract import extract


# from BeautifulSoup import BeautifulSoup
# import pandas as pd

FIND_ELEMENT_TIMEOUT = 30

websiteUrl = 'http://www.flipkart.com'
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(websiteUrl)

try:
    login_popup_close_button = WebDriverWait(driver, FIND_ELEMENT_TIMEOUT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '._2AkmmA._29YdH8')))
except TimeoutException:
    pass
else:
    login_popup_close_button.click()
    print('The Login pop-up was closed.')

try:
    search_input = WebDriverWait(driver, FIND_ELEMENT_TIMEOUT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.LM6RPg')))
except TimeoutException:
    driver.quit()
else:
    search_input.clear()
    search_input.send_keys('laptop')
    print('The search term "laptop" was set.')

searchButton = driver.find_element_by_css_selector(".vh79eN")
searchButton.click();
print('Start to search laptop products.')

allLaptops = []
page_no = 1
next_page_link_xpath = "//nav[@class='_1ypTlJ']/a[@class='_3fVaIS' and span='Next']"
while True:
    current_page_link_xpath = "//nav[@class='_1ypTlJ']/a[@class='_2Xp0TH fyt9Eu' and text()='" + str(page_no) + "']"
    try:
        current_page_link = WebDriverWait(driver, FIND_ELEMENT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, current_page_link_xpath)))
    except TimeoutException:
        break
    else:
        print('Start to handle the data of page ' + str(page_no))

    laptops = extract(driver.page_source)
    for laptop in laptops:
        allLaptops.append(laptop)

    try:
        next_page_link = driver.find_element_by_xpath(next_page_link_xpath)
    except NoSuchElementException:
        print('All pages have been handled')
        break
    else:
        page_no += 1
        next_page_link.click()

print(len(allLaptops))

driver.quit()


