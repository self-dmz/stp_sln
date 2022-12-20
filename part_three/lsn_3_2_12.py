import time
import unittest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def genData():
    faker_ru = Faker('ru_RU')
    yield faker_ru.first_name()


class TestRegForm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_short_reg_form(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        driver = self.browser
        driver.get(link2)
        first_name = driver.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        first_name.send_keys(next(genData()))
        last_name = driver.find_element(By.XPATH, "//label[text()='Last name*']/pyinput")
        last_name.send_keys(next(genData()))
        email = driver.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        email.send_keys(next(genData()))
        phone = driver.find_element(By.XPATH, "//label[text()='Phone:']/following-sibling::input")
        phone.send_keys(next(genData()))
        address = driver.find_element(By.XPATH, "//label[text()='Address:']/following-sibling::input")
        address.send_keys(next(genData()))
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        check_msg = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, check_msg, 'The messages are to be the same.')
        time.sleep(1)

    def test_full_reg_form(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        driver = self.browser
        driver.get(link1)
        first_name = driver.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        first_name.send_keys(next(genData()))
        last_name = driver.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
        last_name.send_keys(next(genData()))
        email = driver.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        email.send_keys(next(genData()))
        phone = driver.find_element(By.XPATH, "//label[text()='Phone:']/following-sibling::input")
        phone.send_keys(next(genData()))
        address = driver.find_element(By.XPATH, "//label[text()='Address:']/following-sibling::input")
        address.send_keys(next(genData()))
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        check_msg = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, check_msg, 'The messages are to be the same.')
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
