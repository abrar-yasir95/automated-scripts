# SHIPPING_METHOD
# Test Case: Visit Product Details page->Select Variant->Select quantity->Scroll down till shipping method->Click
# Select Category->Select Shipping Type-> Select Radio Button-> Apply

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

driver.get("http://localhost:3000/BD_en/products/1ZVFCK4ZCJQAK-new-new-z-warrior-poco-x3-gt-poco-x3-pro-poco-x3-nfc-protective-film/01HGPF9K26335")

print("Starting Test Case")

# variant = driver.find_element(By.XPATH, '')
# variant.click()
# time.sleep(3)
#
# driver.execute_script("window.scrollBy(0, 500);")
# time.sleep(2)
#
method = driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div:nth-child(2) > div:nth-child(3) > div > div.tw-relative > div.tw-relative.tw-grid.tw-grid-cols-12.tw-gap-4 > aside > div > div.tw-border.tw-rounded-lg.tw-p-4.tw-space-y-4 > button > p')
method.click()
time.sleep(2)

# category = driver.find_element(By.CSS_SELECTOR, '')
# category.click()
# time.sleep(2)

# print("Select category below")
# cat = input("Your chosen category")
# time.sleep(2)

# action = ActionChains(driver)
# action.send_keys("hello")
# # action.perform()
# # action.send_keys(Keys.ENTER)
# action.perform()
# action.click()
# time.sleep(2)

# switching to Ship
# ship = driver.find_element(By.XPATH, '')
# ship.click()

#
# # check if cargo, international and P2P are available.
#
# try:
#     xpath1 = '//*[@id="radix-:r8g:"]/div[2]/div[2]/div[3]/div/label[1]/div/div/img'
#     xpath2 = '//*[@id="radix-:r8g:"]/div[2]/div[2]/div[3]/div/label[2]/div/div/div/h2'
#     xpath3 = '//*[@id="radix-:r8g:"]/div[2]/div[2]/div[3]/div/label[3]/div/div/div/h2'
#
#     element1 = driver.find_elements(By.XPATH, xpath1)
#     element2 = driver.find_elements(By.XPATH, xpath2)
#     element3 = driver.find_elements(By.XPATH, xpath3)
#
#     if len(element1) == len(element2) == len(element3) == 3:
#         print("All elements are present, Let's proceed")
#
#     else:
#         print("Expected elements are not present, Pause Here")
#
# finally:
#
#         print("Executed")
#
# # check if the approx weight and shipping cost changes
#
# submit = driver.find_element(By.XPATH, '//*[@id="radix-:rdq:"]/div[2]/div[5]/button[2]')











