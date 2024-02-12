from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

driver = webdriver.Firefox()

driver.get("http://localhost:3000/ship-for-me-v2")

source_country = driver.find_element(By.CSS_SELECTOR, '#test-source-country > button')
time.sleep(2)
source_country.click()
time.sleep(2)

# source
dropdown_element = driver.find_element(By.CSS_SELECTOR, '#test-source-country > select')
#
select = Select(dropdown_element)
selected_option = select.first_selected_option
print("Selected Option:", selected_option.text)

expected_text = "France"
if selected_option.text == expected_text:
    print("Selection successful!")
else:
    print("Selection failed!")

selected_index = select.options.index(selected_option)
print("Selected Index:", selected_index)


# destination
destination_country = driver.find_element(By.CSS_SELECTOR,'#test-warehouse > button')
time.sleep(1)
destination_country.click()
time.sleep(2)

destination_dropdown = driver.find_element(By.CSS_SELECTOR,'#test-warehouse > select')
select = Select(destination_dropdown)
selected_option = select.first_selected_option
print("Selected Option:", selected_option.text)

expected_text = "12"
if selected_option.text == expected_text:
    print("Selection successful!")
else:
    print("Selection failed!")

selected_index = select.options.index(selected_option)
print("Selected Index:", selected_index)


shipping_mode = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > form > div:nth-child(5) > div:nth-child(3) > div')

child_elements = shipping_mode.find_elements(By.XPATH, "./*")


if child_elements:
    time.sleep(3)
    first_child_element = child_elements[2]
    first_child_element.click()
    time.sleep(3)
else:
    print("No child elements found.")


proceed_button = driver.find_element(By.CSS_SELECTOR,'#__next > div > div > div:nth-child(2) > div.tw-bg-white.lg\:tw-bg-\[\#F5F5F5\].tw-py-6 > div > div.tw-block > form > div.tw-flex.tw-justify-end.tw-items-center > div > button')
proceed_button.click()
time.sleep(2)
