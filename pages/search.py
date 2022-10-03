from selenium.webdriver.common.keys import Keys

from constants.search import SearchConsts
from pages.base_page import BasePage


class Search(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = SearchConsts()

    def find_profile(self):
        """Find the profile"""
        self.fill_field(xpath=self.constants.SEARCH_INPUT_FIELD_XPATH, value=self.constants.SEARCH_TEXT + Keys.ENTER)
        self.click(self.constants.SEARCH_RESULT_XPATH)
        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver)
