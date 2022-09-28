import logging

from pages.utils import User

log = logging.getLogger(__name__)


class TestStartPage:

    def test_empty_email_field_alert(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the email field
            Clear the email field
            Check the email-field alert message
        """
        start_page.verify_empty_email_field_alert()

    def test_empty_password_field_alert(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the password field
            Clear the password field
            Check the password-field alert message
        """
        start_page.verify_empty_password_field_alert()

    def test_empty_username_field_alert(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the username field
            Clear the username field
            Check the username-field alert message
        """
        start_page.verify_empty_username_field_alert()

    def test_incorrect_login(self, start_page, random_user):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the username & password fields with random value
            Click on the 'Sign in' button
            Check the invalid username\password alert message
        """
        start_page.sign_in(random_user)

        start_page.verify_sign_in_error()

    def test_empty_login(self, start_page):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Clear the username & password fields
            Click on the 'Sign in' button
            Check the invalid username\password alert message
        """
        start_page.sign_in(User())

        start_page.verify_sign_in_error()

    def test_success_login(self, start_page, known_user):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the username field
            Clear the password field
            Click on the 'Log in' button
            Check if there is a 'Chat' button
        """

        start_page.sign_in(known_user)

        # ToDo fix the test
        start_page.verify_chat_button_exists()

    def test_success_sign_up(self, start_page, random_user):
        """Setup:
            open the qa-complex site
        Steps:
            Fill in the username
            Fill in the email
            Fill in the password
            Click on the Sign-up button"""

        hello_page = start_page.sign_up_and_verify(random_user)

        hello_page.verify_success_sign_up(random_user.username)
