import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://localhost:3000/ship-for-me-v2")

step1 = driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > div:nth-child(3) > div.tw-flex.tw-justify-between.tw-items-center > h2')
print("Step 1")
time.sleep(2)

step2 = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > div:nth-child(4) > div.tw-flex.tw-justify-between.tw-items-center')
print("Step 2")
time.sleep(2)

step3 = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > div:nth-child(5) > div.tw-flex.tw-justify-between.tw-items-center > h2')
print("Step 3")
time.sleep(2)

if step1 in driver.page_source and step2 in driver.page_source and step3 in driver.page_source:
    print("Steps are in order")
else:
    print("Steps are not in order")


edit = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > div:nth-child(5) > div.tw-flex.tw-justify-between.tw-items-center > button]')
edit.click()
time.sleep(2)

address_popup = driver.find_elements(By.CLASS_NAME,'tw-grid tw-grid-cols-1 lg:tw-grid-cols-2 tw-gap-4')
if len(address_popup) >= 2:
    popup_index = random.randint(0,1)
    popup_element = address_popup[popup_index]
    popup_element.click()
    time.sleep(2)

proceed_next = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > div:nth-child(6) > div > div > button')
proceed_next.click()
time.sleep(2)

add_product = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > div.tw-text-center > button')
add_product.click()
time.sleep(2)

update = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > div.tw-flex.tw-justify-between.tw-items-center > div > button')
update.click()
time.sleep(3)
