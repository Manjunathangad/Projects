from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)
print(driver.title)
driver.quit()

