import math
from selenium.common.exceptions import ElementNotVisibleException, ElementNotInteractableException, \
    ElementNotSelectableException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def click_to_login_link(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), 'User is not authorized'

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login button is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except ElementNotVisibleException or \
               ElementNotInteractableException or\
               ElementNotSelectableException:
            return False
        else:
            return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, 1, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what):
        try:
            WebDriverWait(self.browser, timeout=4).until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # gpt version
    def is_disappeared_by_gpt(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout). \
                until(ec.invisibility_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def click_to_basket_link(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()


