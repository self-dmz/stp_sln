import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)

    magic_btn = browser.find_element(By.CSS_SELECTOR, "button[class='trollface btn btn-primary']")
    magic_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")

    result = calc(x.text)

    answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    answer.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text.split()[-1])

finally:
    time.sleep(3)
    browser.quit()

#  При открытии новой вкладки WebDriver продолжит работать со старой вкладкой.
#  Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
#  Это делается с помощью команды switch_to.window:
#  --  browser.switch_to.window(window_name)

#  Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
#  Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
#  --  new_window = browser.window_handles[1]

#  Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
#  --  first_window = browser.window_handles[0]

#  После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.
