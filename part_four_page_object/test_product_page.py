import pytest
from faker import Faker
from part_four_page_object.pages.login_page import LoginPage
from part_four_page_object.pages.product_page import ProductPage

fake = Faker('En')
Faker.seed()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(fake.email(), 'vilk0_qaZ#')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        res = page.should_not_be_success_message()
        assert res, "Success message is presented, but should not be"

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        tb, pb, ta, pa = page.should_be_workable_add_to_basket_button()
        assert tb == ta and pb == pa, 'WRONG book or price in the basket!'


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    empty = page.basket_should_be_empty()
    assert empty, 'The basket contains a stuff, but it is to be empty'


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_workable_add_to_basket_button()
    res = page.should_not_be_success_message()
    print(res)
    assert res, "Success message is presented, but should not be"


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_workable_add_to_basket_button()
    res = page.if_success_message_disappeared()
    assert res, "Success message is presented, but should not be"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_user_cant_see_success_message(self, browser, link):
    page = ProductPage(browser, link)
    page.open()
    res = page.should_not_be_success_message()
    assert res, "Success message is presented, but should not be"


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_user_can_add_product_to_basket(self, browser, link):
    page = ProductPage(browser, link)
    page.open()
    tb, pb, ta, pa = page.should_be_workable_add_to_basket_button()
    assert tb == ta and pb == pa, 'WRONG book or price in the basket!'
