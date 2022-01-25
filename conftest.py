"""
Установка параметров для запуска браузера:
название браузера (выбор Chrome  или Firefox, либо выбор по умолчанию одного
из них, а также выбор языка страницы
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Разбор командной строки и поиск опций:
    {browser_name}
    {language}
    """
    try:
        parser.addoption('--browser_name', action='store', default='chrome',
                        help="Choose browser: chrome or firefox") # выбор браузера
    except:
        pass # если браузер не указан, он определяется в функции browser
    parser.addoption('--language', action='store', default='en',
                      help='Choose language "ru", "en", etc') # выбор языка


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption("browser_name")
    if not browser_name:
        browser_name = 'chrome' # в случае отсутствия выбора в строке
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        opt = Options()
        opt.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}) # передача параметра
        browser = webdriver.Chrome(options=opt)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language) # передача параметра
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

