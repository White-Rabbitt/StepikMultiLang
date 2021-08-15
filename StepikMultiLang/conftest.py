import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Выбор браузера: chrome или firefox")
    parser.addoption('--language', action='store', default='ru', help="выбор языка")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == "chrome":
        print(f'\nЗапуск {browser_name} для теста...')
        browser = webdriver.Chrome()
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError('--browser_name должно быть "chrome"')
    yield browser
    print('\nЗакрытие браузера...')
    browser.quit()
