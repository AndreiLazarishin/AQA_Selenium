from constants.profile_page import ProfileConsts
from pages.hello_page import HelloPage
from pages.utils import log_decorator


class ProfilePage(HelloPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfileConsts

    @log_decorator
    def follow_the_profile(self):
        """Follow the profile"""
        self.click(self.constants.PROFILE_2_FOLLOW_LINK_XPATH)
        self.click(self.constants.FOLLOW_BUTTON_XPATH)
        assert self.is_exists(self.constants.FOLLOW_BUTTON_XPATH)

    @log_decorator
    def unfollow_the_profile(self):
        """Unfollow the profile"""
        self.click(self.constants.PROFILE_2_FOLLOW_LINK_XPATH)
        self.click(self.constants.UNFOLLOW_BUTTON_XPATH)
        assert self.is_exists(self.constants.UNFOLLOW_BUTTON_XPATH)
