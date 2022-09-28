from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage


class CreatePostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConsts()

    def create_post(self, title, body):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=body)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    def verify_successfully_created_message(self):
        """Verify success message"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
 \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    def update_post(self, title, body):
        """Update the post"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=body)
        self.click(xpath=self.constants.UPDATE_POST_BUTTON_XPATH)

    def navigate_to_new_post_page(self):
        self.verify_successfully_created_message()
        from pages.post_page import PostPage
        return PostPage(self.driver)
