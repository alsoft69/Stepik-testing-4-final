from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    BASKET_SUCCESS = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
