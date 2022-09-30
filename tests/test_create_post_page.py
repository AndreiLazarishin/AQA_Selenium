import logging

from pages.utils import Post


class TestCreatePostPage:
    log = logging.getLogger("[CreatePostPage]")

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

        post = Post()
        post.fill_default()
        create_post_page.create_post(post)

        create_post_page.verify_successfully_created_message()
