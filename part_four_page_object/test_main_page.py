import time
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    time.sleep(3)


def test_add_to_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    btn = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    time.sleep(3)
    assert btn.is_displayed()
