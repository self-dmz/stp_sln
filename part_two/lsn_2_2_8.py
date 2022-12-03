import os
from faker import Faker

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def genData():
    faker_ru = Faker('ru_RU')
    yield faker_ru.first_name()


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

    firstname = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    firstname.send_keys(next(genData()))
    lastname = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    lastname.send_keys(next(genData()))
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys(next(genData()))
    attach = browser.find_element(By.CSS_SELECTOR, "input[id='file']")
    attach.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text.split()[-1])


finally:
    time.sleep(3)
    browser.quit()



