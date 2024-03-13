from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest


def pytest_addoption(parser):  # парсер для коммандной строки
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',  # default=Chrome/Firefox, so then I could skip --browser_name  flag in the commandline
                     help="Choose browser: chrome or firefox")
    parser.addoption('--user_language',
                     action='store',
                     default='ru',
                     # default=en/ru, so then I could skip --browser_name  flag in the commandline
                     help="Choose language: en or ru")


@pytest.fixture(scope="function")   # scope="class" or “function”, “module”, “session”
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("user_language")
    # Chrome
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # Firefox
    firefox_options = FirefoxOptions()
    # firefox_options.add_argument('--headless')
    firefox_options.set_preference("intl.accept_languages", user_language)

    if browser_name == "chrome":
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    try:
        yield browser
    finally:
        browser.quit()


@pytest.fixture(autouse=True)  # фикстуру нужно запустить для каждого теста даже без явного вызова
def prepare_data():
    print("preparing some critical data for every test")
