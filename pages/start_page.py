from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_decorator


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants

    @log_decorator
    def sign_in(self, user):
        """Sign in as user"""
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=user.password)
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @log_decorator
    def verify_sign_in_error(self):
        """Verify invalid sign in error"""
        assert self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH) == \
               self.constants.SIGN_IN_LOGIN_ERROR_TEXT, \
            f"Actual message: '{self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH)}'"

    @log_decorator
    def sign_up_and_verify(self, user):
        """Sign up as user and verify that you are inside"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        # Click on the 'sign-up'
        self.click_sign_up_and_verify()
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @wait_until_ok(period=0.25)
    def click_sign_up_and_verify(self):
        """Click sign up button and verify"""
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_exists(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    @log_decorator
    def verify_empty_email_field_alert(self):
        """Verify Empty email error"""
        self.fill_and_clear(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value='email')
        assert self.constants.SIGN_UP_EMAIL_ERROR_TEXT

    @log_decorator
    def verify_empty_password_field_alert(self):
        """Verify Empty email error"""
        self.fill_and_clear(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value='password')
        assert self.constants.SIGN_UP_PASSWORD_ERROR_TEXT

    @log_decorator
    def verify_empty_username_field_alert(self):
        """Verify Empty username error"""
        self.fill_and_clear(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value='1')
        assert self.constants.SIGN_UP_USERNAME_ERROR_TEXT
