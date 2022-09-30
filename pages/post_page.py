from constants.post_page import PostPageConsts
from pages.create_post_page import CreatePostPage
from pages.utils import log_decorator


class PostPage(CreatePostPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostPageConsts

    @log_decorator
    def delete_post(self):
        """"Delete the post"""
        self.click(xpath=self.constants.DELETE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_deleted_post(self):
        """Verify the post was deleted"""
        assert self.get_element_text(xpath=self.constants.SUCCESSFULLY_DELETED_MESSAGE_XPATH) \
               == self.constants.SUCCESSFULLY_DELETED_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESSFULLY_DELETED_MESSAGE_XPATH)}"

    @log_decorator
    def edit_post(self):
        """Find the post and edit it"""
        # self.navigate_to_new_post_page()
        self.click(xpath=self.constants.EDIT_POST_BUTTON_XPATH)
        return CreatePostPage(self.driver)

    @log_decorator
    def verify_successfully_edited_post(self):
        """Verify that post was edited"""
        assert self.get_element_text(xpath=self.constants.SUCCESSFULLY_EDITED_POST_XPATH) \
               == self.constants.SUCCESSFULLY_EDITED_POST_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESSFULLY_EDITED_POST_XPATH)}"
