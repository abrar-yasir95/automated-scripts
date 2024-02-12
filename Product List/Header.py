from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# visit and search for a product
driver = webdriver.Firefox()
driver.get("")
search = driver.find_element(By.XPATH, '')
search.send_keys("shoes")
search.send_keys(Keys.ENTER)

# select checkbox
checkbox_category = driver.find_element(By.XPATH,'')
checkbox_category.click()

view_more = driver.find_element(By.XPATH,'')
view_more.click()

# scroll down

# Destination Point

dest_point = driver.find_element(By.XPATH,'')
dest_point.send_keys("Rajshahi")
dest_point.send_keys(Keys.ENTER)


