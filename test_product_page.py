"""
Модуль по заданию 4.
"""

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/' \
           'catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser)
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_success_messages()
