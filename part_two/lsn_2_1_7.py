import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)

    img = browser.find_element(By.CSS_SELECTOR, "img[id='treasure']")

    x = img.get_attribute('valuex')

    print(x)
    result = calc(int(x))
    print(result)

    answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    answer.send_keys(result)

    imRb = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    imRb.click()

    rbRule = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    rbRule.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']")
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()
    print(alert_text.split()[-1])


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
