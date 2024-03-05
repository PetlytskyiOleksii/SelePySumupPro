import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.base_page import BasePage


params_list = [('?promo=offer0', 'offer0'),
               ('?promo=offer1', 'offer1'),
               ('?promo=offer2', 'offer2'),
               ('?promo=offer3', 'offer3'),
               ('?promo=offer4', 'offer4'),
               ('?promo=offer5', 'offer5'),
               ('?promo=offer6', 'offer6'),
               ('?promo=offer7', 'offer7'),
               ('?promo=offer8', 'offer8'),
               ('?promo=offer9', 'offer9')]


@pytest.mark.smoke
@pytest.mark.parametrize('promo_param, promo_name', params_list, ids=lambda x: x[1])
def test_guest_can_add_product_to_basket(browser, promo_param, promo_name):
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

