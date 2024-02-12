import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

driver.get("http://localhost:3000/ship-for-me-v2")

# navigating next page
# next = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/form/div[5]/div/button')
# next.click()

# random button
details_button = driver.find_elements(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > div:nth-child(4) > div > div')

if details_button:
    random_index = random.randint(0, len(details_button) - 1)
    random_button = details_button[random_index]
    time.sleep(2)

product_link = driver.find_element(By.CSS_SELECTOR,'#product-link')
product_link.click()
product_link.send_keys("https://detail.1688.com/offer/664853648897.html")
time.sleep(2)

product_title = driver.find_element(By.CSS_SELECTOR,'#product-title')
product_title.click()
product_title.send_keys("Shoe")
time.sleep(2)

category = driver.find_element(By.CSS_SELECTOR,'#test-search-input-button')
category.click()
time.sleep(2)

upload = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > form > div.tw-grid.tw-gap-6 > div.tw-flex.tw-items-center.tw-gap-4 > div > div.tw-flex.tw-gap-4.tw-items-center > div > button')
upload.send_keys("D:\Image\Bpaper.jpg")

check_description = driver.find_element(By.CSS_SELECTOR,'#description')
check_description.click()
time.sleep(2)
# color = driver.find_element(By.XPATH,'')
# color.click()
# color.send_keys("red")
description_submit = driver.find_element(By.XPATH,'//*[@id="radix-:r1u:"]/div[2]/div/div/div/div[2]/button')
description_submit.click()
time.sleep(2)

if check_description.is_displayed():
    description_value = check_description.get_attribute("value")
    if description_value:
        print("Input is filled")
    else:
        print("Input field is empty")
else:
    print("Input page is displayed")

    quantity = driver.find_element(By.CSS_SELECTOR,'#quantity')
    quantity.click()
    time.sleep(2)
    quantity_amount = input("Quantity:")
    quantity.send_keys(quantity_amount)
    time.sleep(2)


weight = driver.find_element(By.CSS_SELECTOR,'#weight')
weight.click()
weight.send_keys("5")
time.sleep(2)

measurement = driver.find_element(By.ID,'weightUnits')
select = Select(measurement)
select.select_by_index(1)
time.sleep(2)

length = driver.find_element(By.ID,'length')
length.click()
length.send_keys("20")
time.sleep(2)

measurement_length = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > form > div.tw-grid.tw-gap-6 > div.tw-space-y-4 > div > div.tw-grid.tw-grid-cols-3.tw-gap-2.md\:tw-gap-4 > div:nth-child(1) > div > button')
select = Select(measurement_length)
select.select_by_index(1)
time.sleep(2)

width = driver.find_element(By.ID,'width')
width.click()
width.send_keys("20")
time.sleep(2)

measurement_width = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > form > div.tw-grid.tw-gap-6 > div.tw-space-y-4 > div > div.tw-grid.tw-grid-cols-3.tw-gap-2.md\:tw-gap-4 > div:nth-child(2) > div > button')
select = Select(measurement_width)
select.select_by_index(1)
time.sleep(2)

height = driver.find_element(By.ID,'height')
height.click()
height.send_keys("20")
time.sleep(2)

measurement_height = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > form > div.tw-grid.tw-gap-6 > div.tw-space-y-4 > div > div.tw-grid.tw-grid-cols-3.tw-gap-2.md\:tw-gap-4 > div:nth-child(3) > div > button')
select = Select(measurement_height)
select.select_by_index(1)
time.sleep(2)

price = driver.find_element(By.ID,'price')
price.click()
price.send_keys("20")
time.sleep(2)

price_dropdown = driver.find_element(By.CSS_SELECTOR,'#priceUnits')
select = Select(price_dropdown)
select.select_by_index(0)
time.sleep(2)


currency = driver.find_element(By.ID,'priceUnits')
select = Select(currency)
select.select_by_index(2)
time.sleep(2)

battery = driver.find_element(By.ID,'note')
select = Select(battery)
select.select_by_index(1)
time.sleep(2)

proceed_next = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > div > form > div.tw-flex.tw-justify-between.tw-items-center.tw-mt-8 > div > button')
proceed_next.click()
time.sleep(2)
