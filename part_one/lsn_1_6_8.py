import time, math
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
link = "http://suninjuly.github.io/find_xpath_form"

with driver as browser:
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()
    print(alert_text.split()[-1])
    time.sleep(3)
    browser.quit()
