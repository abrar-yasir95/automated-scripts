from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

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
