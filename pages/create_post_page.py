from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage
from pages.utils import log_decorator


class CreatePostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConsts()

    @log_decorator
    def create_post(self, post):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.click(xpath=self.constants.UNIQUE_POST_CHECKBOX_XPATH)
        self.click(xpath=self.constants.OPTIONS_XPATH)
        self.click(
            xpath=self.constants.VISIBILITY_SELECTION_XPATH.format(option=self.constants.OPTION_PRIVATE_MESSAGE_TEXT))
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    @log_decorator
    def verify_matches_of_the_post(self):
        """Verify the post details"""
        assert self.get_element_text(xpath=self.constants.TITLE_FIELD_XPATH) == self.get_element_text(
            self.constants.CREATED_TITLE_TEXT_XPATH), \
            f"Actual: {self.get_element_text(xpath=self.constants.TITLE_FIELD_XPATH)}"
        assert self.get_element_text(xpath=self.constants.BODY_FIELD_XPATH) == self.get_element_text(
            xpath=self.constants.CREATED_BODY_TEXT_XPATH), \
            f"Actual: {self.get_element_text(xpath=self.constants.BODY_FIELD_XPATH)}"
        assert self.get_element_text(xpath=self.constants.UNIQUE_POST_CHECKBOX_XPATH) == self.get_element_text(
            xpath=self.constants.UNIQUE_CHECKBOX_POSITIVE_TEXT), \
            f"Actual: {self.get_element_text(xpath=self.constants.UNIQUE_POST_CHECKBOX_XPATH)}"
        assert self.get_element_text(xpath=self.constants.OPTION_PRIVATE_MESSAGE) == self.get_element_text(
            xpath=self.constants.OPTION_PRIVATE_MESSAGE_TEXT), \
            f"Actual: {self.get_element_text(xpath=self.constants.OPTION_PRIVATE_MESSAGE)}"

    @log_decorator
    def verify_successfully_created_message(self):
        """Verify success message"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
 \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    @log_decorator
    def update_post(self, post):
        """Update the post"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.click(xpath=self.constants.UPDATE_POST_BUTTON_XPATH)
        from pages.post_page import PostPage
        return PostPage(self.driver)

    @log_decorator
    def navigate_to_new_post_page(self):
        self.verify_successfully_created_message()
        from pages.post_page import PostPage
        return PostPage(self.driver)
