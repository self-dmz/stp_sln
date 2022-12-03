import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
Faker.seed()

def genData():
    faker_ru = Faker('ru_RU')
    yield faker_ru.first_name()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.TAG_NAME, "input")
    print(len(elements))
    for element in elements:
        element.send_keys(next(genData()))

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()
    print(alert_text.split()[-1])

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(13)
    # закрываем браузер после всех манипуляций
    driver.quit()
