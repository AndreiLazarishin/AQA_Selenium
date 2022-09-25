import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import rand_username, rand_email, rand_password, rand_str


class TestCreatePostPage:
    log = logging.getLogger("[CreatePostPage]")

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

    def test_create_post_page(self, hello_page):
        """
            Set up:
                Sign-up\Sign-in as a user
            Steps:
                Navigate to create post page
                Create post
                Verify the result
                """
        create_post_page = hello_page.header.navigate_to_create_post_page()
        self.log.info('Moved to Create Post Page')

        create_post_page.create_post(title=rand_str(23), body=rand_str(150))
        self.log.info('Post created')

        create_post_page.verify_successfully_created_message()
        self.log.info('Message was verified')
