import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.get("http://localhost:3000/product-list")

pagination_class = driver.find_element(By.CLASS_NAME,'tw-grid tw-grid-cols-4 tw-gap-4')
time.sleep(3)

select_product = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#pagination-container-parent > ul > li.tw-border.tw-rounded-md.tw-w-10.tw-h-10.tw-flex.tw-items-center.tw-justify-center.hover\:tw-bg-black.hover\:tw-text-white.pagination-active-child.tw-border.tw-rounded-md.tw-border-black.tw-bg-black.tw-text-white > a')))
driver.execute_script("arguments[0].scrollIntoView(true);", select_product)
time.sleep(3)

select_product.click()

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