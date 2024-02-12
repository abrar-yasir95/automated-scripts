from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

def get_total_api_pages():

    api_url = "https://api.global.sandbox.moveon.work/product-service/api/product/customer/v1/products/search?region=BD&locale=en&page=1&per_page=40"
    response = requests.post(api_url)
    if response.status_code == 200:
        api_data = response.json()
        total_pages = api_data.get("total_pages", 0)
        return total_pages
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

def get_total_ui_pages(driver):
    total_ui_pages = 0
    total_ui_pages_element = driver.find_elements(By.CSS_SELECTOR, "#radix-\:r37\:-content-grid > div.tw-my-8.tw-flex.tw-justify-center > ul > li.tw-border.tw-rounded-md.tw-w-10.tw-h-10.tw-flex.tw-items-center.tw-justify-center.hover\:tw-bg-black.hover\:tw-text-white.tw-border.tw-rounded-md.tw-border-black.tw-bg-black.tw-text-white > a")
    if total_ui_pages_element:
        total_ui_pages = int(total_ui_pages_element.text)
    return total_ui_pages


if __name__ == "__main__":

    driver = webdriver.Firefox()


    driver.get("http://localhost:3000/product-list")


    total_api_pages = get_total_api_pages()

    if total_api_pages is not None:

        total_ui_pages = get_total_ui_pages(driver)


        if total_api_pages == total_ui_pages:
            print("Match: Total pages from API and UI are the same.")
        else:
            print(f"Mismatch: Total pages from API ({total_api_pages}) and UI ({total_ui_pages}) are different.")


