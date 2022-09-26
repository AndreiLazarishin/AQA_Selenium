import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import rand_username, rand_email, rand_password, rand_str


class TestPostPage:
    log = logging.getLogger("[PostPage]")

    @pytest.fixture(scope='function')
    def start_page(self):
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1.5)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture()
    def hello_page(self, start_page):
        """Sign up as a user and return the page"""
        user = rand_username()
        email = rand_email()
        password = rand_password()
        return start_page.sign_up_and_verify(user, email, password)

    @pytest.fixture()
    def create_post_page(self, hello_page):
        """create a post and return the  page"""
        create_post_page = hello_page.header.navigate_to_create_post_page()
        create_post_page.create_post(title=rand_str(23), body=rand_str(150))
        create_post_page.verify_successfully_created_message()
        return create_post_page

    def test_delete_post(self, create_post_page):
        """
                Set up:
                    Sign-up\Sign-in as a user
                    Post some message
                Steps:
                    Navigate to created post page
                    Delete the post
                    Verify the result
               """
        post_page = create_post_page.navigate_to_new_post_page()
        post_page.delete_post()
        self.log.info('Deleting the message')

        post_page.verify_deleted_post()
        self.log.info('The message was deleted')
