import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Выберите браузер: chrome или firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Выберите язык')   


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        print("\nЗапускаем Chrome для теста..")
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        print("\nЗапускаем firefox для теста..")
    else:
        raise pytest.UsageError("--browser_name должен быть chrome или firefox")
    yield browser
    print("\nЗакрываем браузер..")
    browser.quit()