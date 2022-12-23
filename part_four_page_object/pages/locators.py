from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PROCEED_IN_BASKET_BTN = (By.CSS_SELECTOR, "a[class='btn btn-lg btn-primary btn-block']")
    BASKET_LINK_LIST = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE_ON_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, '.product_main p')
    STRONG_LIST = (By.CSS_SELECTOR, 'strong')
    BASKET_LINK_LIST = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class BasketPageLocators():
    PROCEED_IN_BASKET_BTN = (By.CSS_SELECTOR, "a[class='btn btn-lg btn-primary btn-block']")











