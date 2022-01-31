"""
Модуль по заданию 4.
"""

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(browser):
        page = MainPage(browser, link)
        page.open()
        go_to_login_page(browser)


    def go_to_login_page(browser):
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()


    def test_guest_should_see_login_link(browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_should_be_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


def test_should_be_login_form(browser):
    page = LoginPage(browser, link_login)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    page = LoginPage(browser, link_login)
    page.open()
    page.should_be_register_form()
