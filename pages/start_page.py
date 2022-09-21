from time import sleep

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants

    def sign_in(self, username, password):
        """Sign in as user"""
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    def verify_sign_in_error(self):
        """Verify invalid sign in error"""
        assert self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH) == \
               self.constants.SIGN_IN_LOGIN_ERROR_TEXT, \
            f"Actual message: '{self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH)}'"

    def sign_up(self, username, email, password):
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        sleep(1)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        sleep(1)

    def verify_success_sign_up(self, username):
        """Verify success Sign up hello message"""
        username = username.lower()
        assert self.get_element_text(self.constants.HELLO_MESSAGE_XPATH) == \
               self.constants.HELLO_MESSAGE_TEXT.format(username=username), \
            f"Actual message: '{self.get_element_text(self.constants.HELLO_MESSAGE_XPATH)}'"
        assert self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH) == username, \
            f"Actual message: '{self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH)}'"

    def verify_chat_button_exists(self):
        """Verify that chat button exists"""
        assert self.constants.CHAT_BUTTON_EXISTS

    def verify_empty_email_field_alert(self):
        """Verify Empty email error"""
        self.fill_and_clear(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value='email')
        sleep(3)
        assert self.constants.SIGN_UP_EMAIL_ERROR_TEXT

    def verify_empty_password_field_alert(self):
        """Verify Empty email error"""
        self.fill_and_clear(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value='password')
        sleep(3)
        assert self.constants.SIGN_UP_PASSWORD_ERROR_TEXT
