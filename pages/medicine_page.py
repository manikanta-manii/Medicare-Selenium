import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass
from selenium.webdriver.support.select import Select

url = "http://localhost:3000/medicines"


class TestBuyMedicinePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self):
        self.driver.get(url)
        time.sleep(1)

    def add_to_cart(self,count):
        for i in range(1,count+1):
            BaseClass(self.driver, 3).wait_and_click((By.XPATH, f'(//button[@type="submit" and text()="Add to Cart"])[{i}]'))
            print("Medicine added to cart")
        self.driver.get("http://localhost:3000/order_items")
        time.sleep(2)












