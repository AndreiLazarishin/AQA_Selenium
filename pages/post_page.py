from constants.post_page import PostPageConsts
from pages.create_post_page import CreatePostPage


class PostPage(CreatePostPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = PostPageConsts

    def delete_post(self):
        """"Delete the post"""
        self.click(xpath=self.constants.DELETE_POST_BUTTON_XPATH)

    def verify_deleted_post(self):
        """Verify the post was deleted"""
        assert self.get_element_text(xpath=self.constants.SUCCESSFULLY_DELETED_MESSAGE_XPATH) \
               == self.constants.SUCCESSFULLY_DELETED_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESSFULLY_DELETED_MESSAGE_XPATH)}"
