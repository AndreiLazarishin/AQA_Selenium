import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import rand_username, rand_email, rand_password

log = logging.getLogger(__name__)


class TestStartPage:

    @pytest.fixture(scope='function')
    def start_page(self):
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1.5)
        yield StartPage(driver)
        driver.close()

    def test_empty_email_alert(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the email field
            Clear the email field
            Check the email-field alert message
        """
        log.info('Started with empty email')
        start_page.verify_empty_email_field_alert()
        log.info('Empty email field error verified')

    def test_empty_password_alert(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the password field
            Clear the password field
            Check the password-field alert message
        """
        log.info('Getting the error message for the empty password field')
        start_page.verify_empty_password_field_alert()
        log.info('Empty password error verified')

    def test_incorrect_login(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the username & password fields with random value
            Click on the 'Sign in' button
            Check the invalid username\password alert message
        """
        start_page.sign_in('User1', 'Pastor12')
        log.info('Logged in as unknown user')

        start_page.verify_sign_in_error()
        log.info('Error was verified')

    def test_empty_login(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Clear the username & password fields
            Click on the 'Sign in' button
            Check the invalid username\password alert message
        """
        start_page.sign_in('', '')
        log.info('Provided empty values')

        start_page.verify_sign_in_error()
        log.info('Error empty fields was verified')

    def test_success_login(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the username field
            Clear the password field
            Click on the 'Log in' button
            Check if there is a 'Chat' button
        """

        start_page.sign_in('abdul', 'Ci6aZ9khFDWu38L')
        log.info('Logged in as existing user')

        start_page.verify_chat_button_exists()
        log.info('Chat button exists - User is logged in')

    def test_success_sign_up(self, start_page):
        """Setup:
            open the qa-complex site
        Steps:
            Fill in the username
            Fill in the email
            Fill in the password
            Click on the Sign-up button"""
        user = rand_username()
        email = rand_email()
        password = rand_password()
        start_page.sign_up(user, email, password)
        log.info('Filling the fields and sign-up')

        start_page.verify_success_sign_up(user)
        log.info('Sign-up was success')
