from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE_ON_PAGE = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE_ON_PAGE = (By.CSS_SELECTOR, '.product_main p')
    STRONG_LIST = (By.CSS_SELECTOR, 'strong')
    BASKET_LINK_LIST = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    # BOOK_TITLE_IN_BASKET = (By.CSS_SELECTOR, "div[class='col-sm-4'] a:nth-child(1)")
    # BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div[class='col-sm-1'] p[class='price_color align-right']")








