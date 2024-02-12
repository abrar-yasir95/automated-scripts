# vist site, select variant, increase/reduce quantity
# Test Case - Visit Details Page->Select Variant->Increasing Quantity till 4, then decrease by 1

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
print("Test Case started")

# visit site

driver.get("https://ali2bd.com/products/cotton-mens-short-sleeve-t-shirt/AB010-169576519299")

# selecting variant
variant = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/section[1]/div[2]/div/div[4]/div[2]/div[1]/div/div[2]/div[2]/button")
variant.click()
time.sleep(2)

# adding quantity
add = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/section[1]/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[3]/div[1]/button")
add.click()
time.sleep(2)
# variant.send_keys(Keys.PAGE_DOWN)

# m size variant
print("First variant Size M")

# increase
increase = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/section[1]/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[3]/div[1]/div/div[3]/button")
for i in range(3):
    print(f"Increasing Quantity {i + 1}")
    increase.click()
    time.sleep(2)
    print("Decreasing one")
    time.sleep(2)

# decrease
decrease = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/section[1]/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[3]/div[1]/div/div[1]/button")
decrease.click()
time.sleep(2)
print("Second variant size L")

# second variant
variant_l = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/section[1]/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div[1]/button")
variant_l.click()

# increase
increase_l = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/div/section[1]/div[2]/div/div[4]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/div[3]/button")
increase_l.click()
# for a in range(2):
# print(f"Increasing Quantity for L {a + 1}")
# increase_l.click()
# time.sleep(2)

print("Test Case Ends")





