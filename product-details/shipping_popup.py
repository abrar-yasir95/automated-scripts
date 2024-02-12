import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://localhost:3000/product-list")

try:

    elements = driver.find_elements(By.CSS_SELECTOR,'.tw-relative.tw-border.tw-rounded-lg.hover\\:tw-shadow-lg.hover\\:tw-duration-200')
    print("Elements", len(elements))

    random_element = random.choice(elements)

    random_element.click()

    time.sleep(2)

    print("Navigated to a detail page")

except Exception as e:
    print(f"Error: {e}")

finally:
    pass
# driver.get("http://localhost:3000/BD_en/products/1ZVFCK4ZCJQAK-new-new-z-warrior-poco-x3-gt-poco-x3-pro-poco-x3-nfc-protective-film/01HGPF9K26335")

# opening modal
print("Modal is opening")
select_method = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/aside/div/div[1]/button/p')
select_method.click()
print("Modal has opened")
time.sleep(2)

# fetching category
print("Clicking on category field")
category = driver.find_element(By.XPATH,'//*[@id="test-search-input-button"]')
category.click()
time.sleep(2)

# locating field
input_field = driver.find_element(By.XPATH,'//*[@id="test-search-input-field"]')
input_field.click()
time.sleep(2)
field_input = input("Category:")
input_field.send_keys(field_input)
time.sleep(2)


category_element = driver.find_element(By.XPATH,'//*[@id="test-category-blue-bag"]/div')
category_element.click()
time.sleep(2)


# select transport randomly
transport = driver.find_elements(By.CSS_SELECTOR,'#radix-\:r1a\: > div.tw-space-y-4 > div.tw-pt-2 > div:nth-child(1) > div > div')
if transport:
    selected_transport = random.choice(transport)
    selected_transport.click()
    time.sleep(2)


# randomly selecting modes
print("Selecting modes")
elements = driver.find_elements(By.CSS_SELECTOR, '.tw-grid.tw-gap-2.md\:tw-gap-4.tw-grid.tw-grid-cols-1.md\:tw-grid-cols-3')

if elements:
    selected_element = random.choice(elements)
    selected_element.click()
    time.sleep(2)

# submit = driver.find_element(By.CLASS_NAME,'//*[@id="radix-:r1a:"]/div[2]/div[5]/button[2]')
# submit.click()
# time.sleep(1)


