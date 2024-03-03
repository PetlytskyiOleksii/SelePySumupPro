from selenium.common.exceptions import ElementNotVisibleException, ElementNotInteractableException, ElementNotSelectableException, NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except ElementNotVisibleException or \
               ElementNotInteractableException or\
               ElementNotSelectableException:
            return False
        else:
            return True

    def open(self):
        self.browser.get(self.url)