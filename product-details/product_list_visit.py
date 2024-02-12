from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
list_product = driver.find_element(By.XPATH,'https://18b7-113-11-40-254.ngrok-free.app/product-list')
list_product.send_keys(Keys.ENTER)