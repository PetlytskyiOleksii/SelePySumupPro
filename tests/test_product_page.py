import time
import pytest
from pages.basketPage import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.base_page import BasePage

params_list = ['?promo=offer0',
               '?promo=offer1',
               '?promo=offer2',
               '?promo=offer3',
               '?promo=offer4',
               '?promo=offer5',
               '?promo=offer6',
               (pytest.param('?promo=offer7', marks=pytest.mark.xfail)),
               '?promo=offer8',
               '?promo=offer9']


@pytest.mark.parametrize('promo_param', params_list, ids=lambda x: x[-6:])
def test_guest_can_add_product_to_basket(browser, promo_param):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_param}"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasePage(browser, link)
    product_page = ProductPage(browser, link)
    page.open()
    product_page.should_be_add_product_button()
    product_page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_be_message_product_added_to_basket_with_correct_name()
    product_page.should_be_message_with_correct_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasePage(browser, link)
    product_page = ProductPage(browser, link)
    page.open()
    product_page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasePage(browser, link)
    product_page = ProductPage(browser, link)
    page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasePage(browser, link)
    product_page = ProductPage(browser, link)
    page.open()
    product_page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_should_see_login_button_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    login_page = LoginPage(browser, link)
    page.open()
    page.click_to_login_link()
    login_page.should_be_login_page()


@pytest.mark.smoke
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    basket_page = BasketPage(browser, link)
    page.open()
    page.click_to_basket_link()
    basket_page.should_be_empty_basket()


@pytest.mark.logged_user
class TestUserAddToBasketFromProductPage:
    @staticmethod
    @pytest.fixture(scope="function", autouse=True)
    def setup(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = BasePage(browser, link)
        login_page = LoginPage(browser, link)
        page.open()
        page.click_to_login_link()
        login_page.register_new_user(str(time.time()) + '@i.ua', 'login_page_login_page')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = BasePage(browser, link)
        product_page = ProductPage(browser, link)
        page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = BasePage(browser, link)
        product_page = ProductPage(browser, link)
        page.open()
        product_page.should_be_add_product_button()
        product_page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        product_page.should_be_message_product_added_to_basket_with_correct_name()
        product_page.should_be_message_with_correct_product_price()

