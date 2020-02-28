from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ResultPage(BasePage):

    @classmethod
    def phrase_results(cls, phrase):
        xpath = f"//*[contains(text(), '{phrase}')]"
        return By.XPATH, xpath

    def __init__(self, context):
        super().__init__(context.driver)

    def phrase_result_count(self, phrase):
        phrase_results = self.driver.find_elements(*self.phrase_results(phrase))
        return len(phrase_results)

