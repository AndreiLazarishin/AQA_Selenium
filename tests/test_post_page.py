import logging

import pytest

from pages.utils import rand_str, log_decorator


class TestPostPage:
    log = logging.getLogger("[PostPage]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign up as a user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    @pytest.fixture()
    def create_post_page(self, hello_page):
        """create a post and return the  page"""
        create_post_page = hello_page.header.navigate_to_create_post_page()
        create_post_page.create_post(title=rand_str(23), body=rand_str(150))
        create_post_page.verify_successfully_created_message()
        return create_post_page

    @log_decorator
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

        post_page.verify_deleted_post()

    @log_decorator
    def test_edit_post(self, create_post_page):
        """
                Set up:
                    Navigate to the created post page
                Steps:
                    Edit the message
                    Save the changes
        """
        post_page = create_post_page.navigate_to_new_post_page()
        post_page.edit_post()

        post_page.verify_successfully_edited_post()
