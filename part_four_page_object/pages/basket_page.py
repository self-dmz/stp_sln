from part_four_page_object.pages.base_page import BasePage
from part_four_page_object.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty(self):
        return self.is_not_element_present(*BasketPageLocators.PROCEED_IN_BASKET_BTN)

