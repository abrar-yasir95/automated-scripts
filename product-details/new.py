import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://localhost:3000/BD_en/products/1ZVFCK4ZCJQAK-new-new-z-warrior-poco-x3-gt-poco-x3-pro-poco-x3-nfc-protective-film/01HGPF9K26335")

variant = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/section[1]/div/section/div[3]/div[2]/div/div/label/img")
variant.click()
time.sleep(2)

image = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/section[1]/div/aside/div/div[2]/div[1]/div[3]/img")
image.click()
time.sleep(2)

input_quantity = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/section[1]/div/section/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/input')
input_quantity.send_keys("100")
time.sleep(2)

method = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/aside/div/div[1]/button/img')
method.click()
time.sleep(2)

# pr_category = driver.find_element(By.XPATH, '//*[@id="radix-:rs:"]/div[2]/div[1]/div/button')
# pr_category.click()
# time.sleep(2)

