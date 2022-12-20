import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='None', help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    #user_language = request.config.getoption("user_language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # options = Options()
        # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        # options = EdgeOptions()
        # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart firefox browser for test..")
        browser = webdriver.Edge('/media/dmz/HDD/geckodriver/msedgedriver')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
