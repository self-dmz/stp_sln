import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
link = "http://selenium1py.pythonanywhere.com/"
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    @pytest.mark.lnx
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        #browser.find_element(By.CSS_SELECTOR, "button.favorite")
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")

    @pytest.mark.skip
    def test_print_test_msg(self):
        print('SKIP TEST ... ')
