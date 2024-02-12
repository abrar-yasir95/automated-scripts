import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


api_base_url = "https://api.global.sandbox.moveon.work"
ui_url = "http://localhost:3000/product-list"
product_card_class = "tw-grid tw-grid-cols-4 tw-gap-4"


def get_api_count():
    url = "https://api.global.sandbox.moveon.work/product-service/api/product/customer/v1/products/search?region=BD&locale=en&page=1&per_page=40"
    payload = {
        "image_url": "https://cbu01.alicdn.com/img/ibank/2020/800/737/19957737008_43720862.jpg"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Status Code:", response.status_code)

    try:
        response_json = response.json()
        if 'data' in response_json:
            data_array = response_json['data']
            len_count = len(data_array)
            print("Data Count:", len_count)


            for product in data_array:
                if 'price' in product:
                    price = product['price']
                    print("Price:", price)

            return len_count
        else:
            print("No 'data' key found in the response.")
    except json.JSONDecodeError as e:
        print("Unable to decode JSON response:", e)
        print("Response Content:", response.text)

get_api_count()

def get_prices_from_ui(ui_url):
    driver = webdriver.Firefox()
    driver.get(ui_url)
    response = requests.get(ui_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_elements = soup.find_all(class_=product_card_class)

        price_count = len(price_elements)
        print("Price count", price_count)
        for price_element in price_elements:
            price = price_element.text.strip()
            print("Price", price)
        driver.quit()
        return price_count

def main():
    try:

        api_count = get_api_count()
        price_count = get_prices_from_ui(ui_url)

        if api_count == price_count:
            print("Prices are matched")
        else:
             print("Prices are not matched")
    except Exception as e:
          print(f"Error: {e}")

if __name__ == "__main__":
    main()


