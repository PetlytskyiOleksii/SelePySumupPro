import time

import pytest
from pages.main_page import MainPage
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


@pytest.mark.skip
@pytest.mark.parametrize('promo_param', params_list, ids=lambda x: x[-6:])
def test_guest_can_add_product_to_basket(browser, promo_param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo_param}"
    page = MainPage(browser, link)
    base_page = BasePage(browser, link)
    product_page = ProductPage(browser, link)
    page.open()
    product_page.should_be_add_product_button()
    product_page.add_product_to_basket()
    base_page.solve_quiz_and_get_code()
    product_page.should_be_message_product_added_to_basket_with_correct_name()
    product_page.should_be_message_with_correct_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    base_page = BasePage(browser, link)
    product_page = ProductPage(browser, link)
    base_page.open()
    product_page.add_product_to_basket()
    base_page.solve_quiz_and_get_code()
    # time.sleep(10000)
    product_page.should_not_be_success_message()


@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    base_page = BasePage(browser, link)
    product_page = ProductPage(browser, link)
    base_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    base_page = BasePage(browser, link)
    product_page = ProductPage(browser, link)
    base_page.open()
    product_page.add_product_to_basket()
    base_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()
