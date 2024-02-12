# vist site, select variant, increase/reduce quantity
# Test Case - Visit Details Page->Select Variant->Increasing Quantity, check the slot, decrease variant
# then scroll down and check specs, details and reviews.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
print("Test Case started")

# visit site

driver.get("http://localhost:3000/BD_en/products/1ZVFCK4ZCJQAK-new-new-z-warrior-poco-x3-gt-poco-x3-pro-poco-x3-nfc-protective-film/01HGPF9K26335")

# selecting variant
variant = driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div:nth-child(2) > div:nth-child(3) > div > div.tw-relative > div.tw-relative.tw-grid.tw-grid-cols-12.tw-gap-4 > div > section.tw-space-y-6 > div > section > div.tw-space-y-4 > div.tw-space-y-4 > div > div > label > img')
variant.click()
time.sleep(2)

# image select
image_select = driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div:nth-child(2) > div:nth-child(3) > div > div.tw-relative > div.tw-relative.tw-grid.tw-grid-cols-12.tw-gap-4 > div > section.tw-space-y-6 > div > aside > div > div.swiper.swiper-initialized.swiper-horizontal.mySwiper.swiper-backface-hidden > div.swiper-wrapper > div.swiper-slide.tw-border-2.tw-p-0\.5.tw-rounded-lg.hover\:tw-border-mvnGreen.tw-border-mvnGreen > img')
image_select.click()
time.sleep(2)

# adding quantity
# add = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/section[1]/div/section/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/button[2]/svg')
# add.click()
# time.sleep(2)
# variant.send_keys(Keys.PAGE_DOWN)

# m size variant
# print("First variant Size M")

# increase quantity
# increase = driver.find_element(By.CSS_SELECTOR, '#__next > div > div > div:nth-child(2) > div:nth-child(3) > div > div.tw-relative > div.tw-relative.tw-grid.tw-grid-cols-12.tw-gap-4 > div > section.tw-space-y-6 > div > section > div.tw-space-y-4 > div:nth-child(3) > div > div.tw-max-h-\[264px\].tw-overflow-y-scroll.tw-overflow-x-hidden > div > div:nth-child(1) > div.tw-flex.tw-col-span-4.tw-justify-center > button:nth-child(3)')
# for i in range(10):
#     print(f"Increasing Quantity {i + 1}")
#     increase.click()
#     time.sleep(2)
#     # print("Decreasing one")
#     # time.sleep(2)

input_quantity = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/section[1]/div/section/div[3]/div[3]/div/div[2]/div/div[1]/div[2]/input')
input_quantity.send_keys("100")
time.sleep(2)

# decrease
# decrease = driver.find_element(By.CSS_SELECTOR, "#__next > div > div > div:nth-child(2) > div:nth-child(3) > div > div.tw-relative > div.tw-relative.tw-grid.tw-grid-cols-12.tw-gap-4 > div > section.tw-space-y-6 > div > section > div.tw-space-y-4 > div:nth-child(3) > div > div.tw-max-h-\[264px\].tw-overflow-y-scroll.tw-overflow-x-hidden > div > div:nth-child(2) > div.tw-flex.tw-col-span-4.tw-justify-center > button:nth-child(1) > svg")
# decrease.click()
# time.sleep(2)

# show_more = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/section[1]/div/section/div[3]/div[3]/div/div[3]/button')
# show_more.click()
# time.sleep(2)
# # show_more.send_keys(Keys.PAGE_DOWN)
#
# show_less = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/section[1]/div/section/div[3]/div[3]/div/div[3]/button')
# show_less.click()
# time.sleep(2)









# second variant
# variant_l = driver.find_element(By.XPATH, "")
# variant_l.click()

# increase
# increase_l = driver.find_element(By.XPATH,"")
# increase_l.click()
# for a in range(2):
# print(f"Increasing Quantity for L {a + 1}")
# increase_l.click()
# time.sleep(2)

# show more
# more = driver.find_element(By.XPATH,'')
# more.click()
#
# print("Test Case Ends")





