import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


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
            print("Data Count:",len_count)
            # print(json.dumps(data_array, indent=2))
            return len_count
        else:
            print("No 'data' key found in the response.")
    except json.JSONDecodeError as e:
        print("Unable to decode JSON response:", e)
        print("Response Content:", response.text)


def get_ui_count():
    driver = webdriver.Firefox()
    driver.get(ui_url)

    driver.implicitly_wait(10)

    # class_name = "tw-grid tw-grid-cols-4 tw-gap-4"
    products_container = driver.find_element(By.CLASS_NAME, 'products-list-container')
    child_elements = products_container.find_elements(By.XPATH, './*')

    return len(child_elements)


def main():
    try:
        api_count = get_api_count()
        ui_count = get_ui_count()
        if api_count == ui_count:
            print("Products are matched")
        else:
             print("Products are not matched")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()



