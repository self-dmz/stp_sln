

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_on_page_add_to_basket(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button != None, "Button 'Add to basket' is not on page"
