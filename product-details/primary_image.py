import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://localhost:3000/BD_en/products/NGDZ0CTYEXK61-handheld-folding-led-reading-new-collection-birthday-gift/01HGPFB543Z0R"

driver = webdriver.Firefox()
driver.get(url)

thumbnail_elements = driver.find_elements(By.CLASS_NAME, "tw-rounded-md.tw-w-full.tw-h-full")  
primary = driver.find_element(By.CLASS_NAME, "tw-w-full.tw-h-auto.tw-rounded-lg")

def get_primary_image_source():
    return primary.get_attribute("src")

try:
    for index, thumbnail in enumerate(thumbnail_elements):

        driver.execute_script("arguments[0].click();", thumbnail)
        time.sleep(5)


        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "tw-w-full.tw-h-auto.tw-rounded-lg")))


        print(f"Thumbnail {index + 1} - Current primary image source:", get_primary_image_source())

finally:
    pass
