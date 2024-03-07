from pages.base_page import BasePage
import pytest
from pages.login_page import LoginPage
from pages.basketPage import BasketPage


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    login_page = LoginPage(browser, link)
    page.open()
    page.click_to_login_link()
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.smoke
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    basket_page = BasketPage(browser, link)
    page.open()
    page.click_to_basket_link()
    basket_page.should_be_empty_basket()
