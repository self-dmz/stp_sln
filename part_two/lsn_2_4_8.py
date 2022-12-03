import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    book = browser.find_element(By.CSS_SELECTOR, "button[id='book']")
    book.click()

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")

    result = calc(x.text)

    answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    answer.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, "button[id='solve']")
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text.split()[-1])

finally:
    time.sleep(3)
    browser.quit()


