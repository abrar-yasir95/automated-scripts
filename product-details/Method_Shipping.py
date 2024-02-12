import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://localhost:3000/BD_en/products/1ZVFCK4ZCJQAK-new-new-z-warrior-poco-x3-gt-poco-x3-pro-poco-x3-nfc-protective-film/01HGPF9K26335")

print("Test Case Started")
print("Opening Shipping Method modal")

method = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/aside/div/div[1]/button/img')
method.click()
time.sleep(2)

category = driver.find_element(By.XPATH,'//*[@id="radix-:r6:"]/div[2]/div[1]/div/button')
category.click()
time.sleep(2)
category_field = driver.find_element(By.XPATH, '//*[@id="radix-:r6:"]/div[2]/div[1]/div/div/div[1]/input')
category_field.click()
time.sleep(2)

category.send_keys("Blue Bag")
category.send_keys(Keys.ENTER)

# switching to Ship
# ship = driver.find_element(By.XPATH, '//*[@id="radix-:r9:-trigger-By Ship"]')
# ship.click()

# Air, cargo, international and p2p should be selected.
# try:
#     xpath1 = '//*[@id="radix-:r8g:"]/div[2]/div[2]/div[3]/div/label[1]/div/div/img'
#     xpath2 = '//*[@id="radix-:r8g:"]/div[2]/div[2]/div[3]/div/label[2]/div/div/div/h2'
#     xpath3 = '//*[@id="radix-:r8g:"]/div[2]/div[2]/div[3]/div/label[3]/div/div/div/h2'
#
#     element1 = driver.find_elements(By.XPATH, xpath1)
#     element2 = driver.find_elements(By.XPATH, xpath2)
#     element3 = driver.find_elements(By.XPATH, xpath3)
#
#     if len(element1) == len(element2) == len(element3) == 3:
#         print("All elements are present, Let's proceed")
#
#     else:
#         print("Expected elements are not present, Pause Here")
#
# finally:
#
#         print("Executed")

# cargo company
# c_company = driver.find_element(By.CSS_SELECTOR,'#radix-\:r6\: > div.tw-space-y-4 > div.tw-pt-2 > div:nth-child(3) > div > label:nth-child(1) > div > div')
# c_company.click()
# #
# # select warehouse agent
# warehouse_agent = driver.find_element(By.CSS_SELECTOR,'#radix-\:r6\: > div.tw-space-y-4 > div.tw-bg-\[\#F5F5F5\].tw-p-\[10px\].tw-rounded-md.tw-space-y-3 > div:nth-child(2) > div > div > label > div > div > div > div.tw-flex.tw-items-center.tw-gap-4')
# warehouse_agent.click()
#
# submit
submit = driver.find_element(By.CSS_SELECTOR,'#radix-\:r6\: > div.tw-space-y-4 > div.tw-flex.tw-flex-col-reverse.sm\:tw-flex-row.sm\:tw-justify-end.sm\:tw-space-x-2.sm\:justify-start > button.tw-inline-flex.tw-items-center.tw-justify-center.tw-rounded-lg.tw-text-sm.tw-font-medium.tw-ring-offset-background.tw-transition-colors.focus-visible\:tw-outline-none.focus-visible\:tw-ring-2.focus-visible\:tw-ring-ring.focus-visible\:tw-ring-offset-2.disabled\:tw-pointer-events-none.disabled\:tw-opacity-50.tw-bg-mvnGreen.tw-text-white.tw-h-10.tw-px-4.tw-py-2')
submit.click()

