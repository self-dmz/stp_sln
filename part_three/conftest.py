import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', '--language', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Language parameter is to be set")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome" and language:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart firefox browser for test..")
        browser = webdriver.Edge('/media/dmz/HDD/geckodriver/msedgedriver', options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or edge")
    yield browser
    print("\nquit browser..")
    browser.quit()
