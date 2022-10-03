from constants.my_profile_page import ProfileConsts
from pages.hello_page import HelloPage


class ProfilePage(HelloPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfileConsts

    def follow_the_profile(self, profile):
        """Follow the profile"""
        self.click(self.constants.PROFILE_2_FOLLOW_LINK_XPATH)
        self.click(self.constants.FOLLOW_BUTTON_XPATH)
        assert self.is_exists(self.constants.FOLLOW_BUTTON_XPATH)
