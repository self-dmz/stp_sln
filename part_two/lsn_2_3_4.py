import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)

    magic_btn = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    magic_btn.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    #print(alert_text.split()[-1])

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")

    result = calc(x.text)

    answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    answer.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    submit.click()

    alert2 = browser.switch_to.alert
    alert_text2 = alert.text
    alert2.accept()
    print(alert_text2.split()[-1])

finally:
    time.sleep(3)
    browser.quit()
