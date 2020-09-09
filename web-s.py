from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

try:
    search_result_summary_element = WebDriverWait(driver, FIND_ELEMENT_TIMEOUT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '._2yAnYN')))
except TimeoutException:
    driver.quit()
else:
    print(search_result_summary_element.get_attribute('innerText'))

driver.quit()


