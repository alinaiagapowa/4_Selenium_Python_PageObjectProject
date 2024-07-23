from pages.base_page import BasePage
import time

def test_should_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasePage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(10)