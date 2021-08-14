import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome', help='Выбор браузера: Chrome или Firefox')
    parser.addoption('--language', action='store', default='ru', help='Choose language')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    lang = request.config.getoption("language")
    if browser_name == "Chrome":
        chrome_bro = Options()
        print(f'\nЗапуск {browser_name} для теста...')
        browser = webdriver.Chrome(options=chrome_bro)
    elif browser_name == "Firefox":
        firefox_profile = webdriver.FirefoxProfile()
        print(f'\nЗапуск {browser_name} для теста...')
        browser = webdriver.Firefox()
    else:
        print(f'Браузер {browser_name} ещё не готов')
        browser = None
    yield browser
    print("\nЗакрытие браузера...")
    time.sleep(2)
    browser.quit()
