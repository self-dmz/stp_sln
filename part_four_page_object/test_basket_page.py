from part_four_page_object.pages.basket_page import BasketPage


def test_if_basket_is_empty(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_the_basket()
    empty = page.is_basket_empty()
    assert empty, 'Basket is NOT empty but it should be'
