from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

driver = webdriver.Firefox() #Opera(executable_path=OperaDriverManager().install())



driver.get("https://stepik.org/lesson/25969/step/8")
