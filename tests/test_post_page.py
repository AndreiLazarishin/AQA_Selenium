import logging

import pytest

from pages.utils import Post


class TestPostPage:
    log = logging.getLogger("[PostPage]")

    @pytest.fixture()
    def create_post_page(self, hello_page):
        """create a post and return the  page"""
        create_post_page = hello_page.header.navigate_to_create_post_page()
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)
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

        post_page.verify_deleted_post()

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
