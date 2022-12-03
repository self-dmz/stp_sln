import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)

    browser.execute_script("document.getElementsByClassName('bd-footer bg-light text-muted')[0].remove();")

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")

    result = calc(x.text)

    answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    answer.send_keys(result)

    imRb = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    imRb.click()

    rbRule = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    rbRule.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text.split()[-1])


finally:
    time.sleep(3)
    browser.quit()
