import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    basket_button = browser.find_elements_by_css_selector("button[type='submit'].btn-add-to-basket")
    assert basket_button == "Добавить в корзину"
