from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .BasePage import BasePage


class SearchPage(BasePage):

    SEARCH_INPUT = (By.XPATH, "//input[@name='q']")

    def __init__(self, context):
        super().__init__(context.driver)

    def search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
