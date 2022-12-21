import time
import pytest
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_url_should_be_present_in_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    time.sleep(3)


def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    time.sleep(3)
