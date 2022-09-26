from constants.my_profile_page import MyProfileConsts
from pages.hello_page import HelloPage


class MyProfilePage(HelloPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MyProfileConsts
