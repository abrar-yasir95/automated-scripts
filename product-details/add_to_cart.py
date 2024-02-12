# ADD_TO_CART

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://localhost:3000/BD_en/products/1ZVFCK4ZCJQAK-new-new-z-warrior-poco-x3-gt-poco-x3-pro-poco-x3-nfc-protective-film/01HGPF9K26335")

# variant = driver.find_element(By.XPATH, '')
# variant.click()
# time.sleep(3)
#
# plus_button = driver.find_element(By.CSS_SELECTOR,'' )
# plus_button.click()
# time.sleep(3)
#
# add = driver.find_element(By.XPATH, '')
# add.click()
# time.sleep(2)
#
# visit_cart = driver.find_element(By.XPATH, '')
# visit_cart.click()
# time.sleep(2)
# radio_button = driver.find_element(By.ID, 'cart_item-240390')
# radio_button.click()
#
# delete = driver.find_element(By.XPATH,'')
# delete.click()

add_to_cart = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/aside/div/div[1]/div/div[5]/button[2]')
add_to_cart.click()
