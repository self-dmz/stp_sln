import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()

    browser.get(link)

    num_1 = browser.find_element(By.CSS_SELECTOR, "span[id='num1']")
    num_2 = browser.find_element(By.CSS_SELECTOR, "span[id='num2']")

    select = Select(browser.find_element(By.CSS_SELECTOR, "select[id='dropdown']"))

    select.select_by_value(str(int(num_1.text) + int(num_2.text)))

    submit = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']")
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text.split()[-1])


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
