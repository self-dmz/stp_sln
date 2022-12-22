# import time
# import math
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
#                                   "https://stepik.org/lesson/236896/step/1",
#                                   "https://stepik.org/lesson/236897/step/1",
#                                   "https://stepik.org/lesson/236898/step/1",
#                                   "https://stepik.org/lesson/236899/step/1",
#                                   "https://stepik.org/lesson/236903/step/1",
#                                   "https://stepik.org/lesson/236904/step/1",
#                                   "https://stepik.org/lesson/236905/step/1"])
# def test_open_diff_link_on_stepik(browser, link):
#     browser.get(link)
#     login = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='ember33']")))
#     login.click()
#     email = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='id_login_email']")))
#     email.send_keys('email')
#     psw = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='id_login_password']")))
#     psw.send_keys('psw')
#     WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти']"))).click()
#     text_area = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ember-text-area')))
#     text_area.send_keys(math.log(int(time.time())))
#     button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'submit-submission')))
#     button.click()
#     assert WebDriverWait(browser, 15).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))).text == 'Correct!'
import math

from selenium.common import NoAlertPresentException


def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

print(str(math.log(abs((12 * math.sin(float(333)))))))
