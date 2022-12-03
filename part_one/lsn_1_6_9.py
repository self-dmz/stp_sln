import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def genData():
    faker_ru = Faker('ru_RU')
    yield faker_ru.first_name()

try:
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(link1)

    first_name = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
    first_name.send_keys(next(genData()))

    last_name = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
    last_name.send_keys(next(genData()))

    email = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
    email.send_keys(next(genData()))

    phone = browser.find_element(By.XPATH, "//label[text()='Phone:']/following-sibling::input")
    phone.send_keys(next(genData()))

    address = browser.find_element(By.XPATH, "//label[text()='Address:']/following-sibling::input")
    address.send_keys(next(genData()))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
