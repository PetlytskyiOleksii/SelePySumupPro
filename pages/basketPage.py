from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text == "Your basket is empty. Continue shopping", \
            'Basket is not empty but it should'

