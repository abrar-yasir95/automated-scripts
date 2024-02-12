import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

api_url = "https://api.global.sandbox.moveon.work/product-service/api/product/customer/v1/products/search?region=BD&locale=en&page=1&per_page=40"
response = requests.post(api_url)

try:
    response.raise_for_status()
    api_data = response.json()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error", errh)
except requests.exceptions.RequestException as err:
    print("Request Error:", err)
except json.decoder.JSONDecodeError as json_err:
    print("JSON Decode Error. Response content:", response.text)
    exit(1)


driver = webdriver.Firefox()
web_url = "http://localhost:3000/product-list"
driver.get(web_url)

product_card_selector = "#products-list-container > div:nth-child(1) > a > div > figure > img"

try:
    product_card = driver.find_element(By.CSS_SELECTOR,product_card_selector)
except NoSuchElementException:
    print("Product Card Not found in webpage")
    exit(1)

product_position = product_card.location
expected_position = api_data.get("position")

if product_position == expected_position:
    print("Matched")
else:
    print("Did not matched")
