# review, details, spec
# Test Case: Visit Details Page->Select Variant->Scroll Down till Specification-> Select Spec at first
# Go down->Go up and select Product Details->Then select Reviews

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://localhost:3000/BD_en/products/1ZVFCK4ZCJQAK-new-new-z-warrior-poco-x3-gt-poco-x3-pro-poco-x3-nfc-protective-film/01HGPF9K26335")
print("Starting Test Case")
variant = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/section[1]/div/section/div[3]/div[2]/div/div/label/img')
variant.click()
time.sleep(3)

# specification
element = driver.find_element(By.XPATH, '//*[@id="radix-:r2:-trigger-specification"]')
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
time.sleep(4)

# element1 = driver.find_element(By.XPATH, '//*[@id="react-tabs-1"]/div/div/table/tbody/tr[38]/td')
# driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element1)
# time.sleep(4)
#
# element_up = driver.find_element(By.XPATH, '//*[@id="react-tabs-2"]')
# driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center' });", element_up)
# time.sleep(2)

# product details
detail = driver.find_element(By.XPATH,'//*[@id="radix-:r2:-trigger-product-details"]')
detail.click()
time.sleep(3)

# reviews

review = driver.find_element(By.XPATH, '//*[@id="radix-:r2:-trigger-reviews"]')
review.click()
time.sleep(3)


