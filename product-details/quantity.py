import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://localhost:3000/BD_en/products/NGDZ0CTYEXK61-handheld-folding-led-reading-new-collection-birthday-gift/01HGPFB543Z0R")

time.sleep(2)

image_elements = driver.find_elements(By.CLASS_NAME,'tw-rounded-md.tw-w-full.tw-h-full')
random_image = random.choice(image_elements)
random_image.click()
time.sleep(2)

quantity_input = driver.find_element(By.XPATH,'//*[@id="variation"]/div/div/div[2]/button[2]')
quantity_input.click()
time.sleep(2)

# quantity_input.clear()
# quantity_input.send_keys("2")

quantity_input.send_keys(Keys.ENTER)
time.sleep(4)
