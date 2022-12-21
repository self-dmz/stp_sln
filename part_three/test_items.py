from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/




def test_add_to_basket_button(browser):
    browser.get(link)
    add_btn = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    print(add_btn.text)



