import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox()      # browser_is_opened
driver.maximize_window()
driver.get("https://www.groww.in")     # Groww_open
time.sleep(3)
search_button = driver.find_element(By.XPATH,'//input[@id="globalSearch23"]')
search_button.click()
search_button.send_keys("Cochin Shipyard")
time.sleep(3)
search_button.send_keys(Keys.ENTER)
time.sleep(3)
driver.execute_script(f"window.scrollBy(0, {2000});")
time.sleep(2)
fundamentals = h2_element = driver.find_element(By.XPATH, '//h2[text()="Fundamentals"]')
content = fundamentals.text
print(content)
fundamentals_content = driver.find_element(By.XPATH,'//table[@class="tb10Table col l12 ft785Table"]')
fundamentalscontent = fundamentals_content.text
print(fundamentalscontent)









