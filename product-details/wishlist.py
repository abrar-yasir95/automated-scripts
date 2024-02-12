# wishlist, share, seller, spec
# Test Case - Click on Wishlist icon->Visit Wishlist page & then click on share icon->

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.maximize_window()
print("Starting Test Case")
driver.get("https://moveon.com.bd/product?url=https%3A%2F%2Fdetail.1688.com%2Foffer%2F532600651915.html")
# wishlist
wishlist = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[2]/button")
wishlist.click()
print(" Selected for wishlist")
time.sleep(4)
wishlist_list = driver.find_element(By.XPATH, "https://moveon.com.bd/wish-list")
time.sleep(2)
driver.back()
print("Returned to previous page")


# #share
# driver.get("")
# share = driver.find_element(By.XPATH, "")
# share.click()
# # time.sleep(2)
# social = driver.find_element(By.XPATH, "")
# social.click()



