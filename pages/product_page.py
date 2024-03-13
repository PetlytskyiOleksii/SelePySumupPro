from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        return str(product_name)

    def get_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        return str(product_price)

    def should_be_add_product_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add product button is absent on the product page'

    def should_be_message_product_added_to_basket_with_correct_name(self):
        assert f"{self.get_product_name()} has been added to your basket." in self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE).text, \
            'message is incorrect after adding a product to basket'

    def should_be_message_with_correct_product_price(self):
        assert self.get_product_price() == self.browser.find_element(
            *ProductPageLocators.TOTAL_BASKET_PRICE_MESSAGE).text, \
            'price in basket is incorrect'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE), "success message is present but shouldn't"

    def should_not_be_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE), "success message is not disappear but should"
