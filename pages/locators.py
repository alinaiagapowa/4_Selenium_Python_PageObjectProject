from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_PROD_1 = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    TEXT_ADD_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    TEXT_PROD = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')

    AMOUNT_BASKET = (By.CSS_SELECTOR, '.alert-info.fade.in > div > p:nth-child(1) > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')