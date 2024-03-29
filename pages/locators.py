from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket')]//a")
    USER_ICON = By.CSS_SELECTOR, ".icon-user"


class LoginPageLocators:
    LOGIN_FROM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    CONFIRM_REGISTRATION_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
    SUBMIT_REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]")  # get text
    TOTAL_BASKET_PRICE_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket total is now ')]//strong")  # get text


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner')
