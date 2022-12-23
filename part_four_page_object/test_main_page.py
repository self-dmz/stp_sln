import time

import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    is_basket_empty = page.basket_should_be_empty()
    print('Empty basket ?', is_basket_empty)
    assert is_basket_empty is not True, 'The basket contains a stuff, but it is to be empty'


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #wl = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer '
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    time.sleep(3)

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    wl = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer '
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_add_to_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    wl = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer '
    browser.get(link)
    btn = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    time.sleep(3)
    assert btn.is_displayed()
