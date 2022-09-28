import logging

import pytest

from pages.utils import rand_str, User


class TestCreatePostPage:
    log = logging.getLogger("[CreatePostPage]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign up as a user and return the page"""
        user = User()
        user.fill_data()
        return start_page.sign_up_and_verify(random_user)

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
