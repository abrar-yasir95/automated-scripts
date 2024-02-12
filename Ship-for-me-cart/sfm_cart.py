import time
import random
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://localhost:3000/ship-for-me-v2")

shipment_list = driver.find_elements(By.CLASS_NAME, ' tw-grid tw-grid-cols-1 tw-gap-1')
if not shipment_list:
    print("No elements found")
else:
    random_element = random.choice(shipment_list)
    random_element.click()

radio_button_class = driver.find_elements(By.CLASS_NAME,
                                          'tw-peer tw-h-6 tw-w-6 lg:tw-h-4 lg:tw-w-4 tw-shrink-0 tw-rounded-sm tw-border tw-bg-white tw-border-inherit tw-ring-offset-background focus-visible:tw-outline-none focus-visible:tw-ring-2 focus-visible:tw-ring-ring focus-visible:tw-ring-offset-2 disabled:tw-cursor-not-allowed disabled:tw-opacity-50 data-[state=checked]:tw-bg-mvnGreen-800 data-[state=checked]:tw-border-mvnGreen-800 data-[state=checked]:tw-text-white hover:tw-border-mvnGreen-800 hover:tw-bg-mvnGreen-25 tw-duration-100')
if not radio_button_class:
    print("No radio buttons found")
else:
    random_radio_button = random.choice(radio_button_class)

    if not random_radio_button.is_selected():
        random_radio_button.click()
        print("Radio button is selected")

    edit_icon = random_radio_button.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[3]/div/div[5]/form/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/button[2]')
    edit_icon.click()
    time.sleep(2)
    print("Edit icon is clicked")

    subprocess.run(['python','step_one.py'])

    copy_icon = random_radio_button.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[3]/div/div[5]/form/div[2]/div[10]/div[2]/div[2]/div[2]/div[2]/button[1]')
    copy_icon.click()
    time.sleep(2)
    print("Item Copied")

    popup_message_locator = (By.XPATH,'')
    popup_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located(popup_message_locator))
    assert "Shipping cart item cloned successfully" in popup_message.text
    print("Verified popup message",popup_message.text)

    delete_icon = random_radio_button.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[3]/div/div[5]/form/div[2]/div[10]/div[2]/div[2]/div[2]/div[2]/button[3]')
    delete_icon.click()
    time.sleep(2)
    print("Delete popup")

    locate_yes = driver.find_element(By.XPATH,'//*[@id="radix-:r1d:"]/div[2]/button[2]')
    locate_yes.click()
    time.sleep(2)

    submit_request = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[3]/div/div[5]/form/div[3]/div/button')
    submit_request.click()
    time.sleep(2)




