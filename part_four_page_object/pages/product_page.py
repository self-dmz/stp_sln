import time

from part_four_page_object.pages.base_page import BasePage
from part_four_page_object.pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_workable_add_to_basket_button(self):
        title_before = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_ON_PAGE).text
        price_before = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE).text
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()
        lst = self.browser.find_elements(*ProductPageLocators.STRONG_LIST)
        title_after = lst[3].text
        price_after = lst[5].text
        return title_before, price_before, title_after, price_after

    def should_not_be_success_message(self):
        return self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def if_success_message_disappeared(self):
        return self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)






