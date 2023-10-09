import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox()      # browser_is_opened
driver.maximize_window()
driver.get("https://www.groww.in")     # Groww_open
time.sleep(1)
search_button = driver.find_element(By.XPATH,'//input[@id="globalSearch23"]')
search_button.click()
search_button.send_keys("Cochin Shipyard")
time.sleep(1)
search_button.send_keys(Keys.ENTER)
time.sleep(1)
driver.execute_script(f"window.scrollBy(0, {2000});")
time.sleep(1)
print("Fundamentals of the company")
fundamentals_content_element = driver.find_element(By.XPATH,'//table[@class="tb10Table col l12 ft785Table"]')
fundamentals_content = fundamentals_content_element.text
print(fundamentals_content)
driver.execute_script(f"window.scrollBy(0, {800});")
time.sleep(1)
read_more = driver.find_element(By.XPATH,'//div[@class="rm14ReadDiv backgroundPrimary cur-po contentAccent rm14ReadMore pos-abs bodyMedium16"]')
read_more.click()
data = driver.find_element(By.XPATH,'//div[@class="pos-rel rm14MainContainer"]')
content1 = data.text
print("About the Company")
print(content1)
driver.execute_script(f"window.scrollBy(0, {1400});")
time.sleep(2)
faq = driver.find_element(By.XPATH,'//h3[text()="What is the Share Price of Cochin Shipyard?"]')
faq.click()
time.sleep(2)
ans = driver.find_element(By.XPATH,'//div[@class="ac11RevealComplete ac11Show"]')
print("Current Share Price")
print(ans.text)
more_data = driver.find_element(By.XPATH,'//div[@class="col l12 contentPrimary"]')
print(more_data.text)


