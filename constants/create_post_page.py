class CreatePostPageConsts:
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    CREATED_TITLE_TEXT_XPATH = ".//h2"
    BODY_FIELD_XPATH = ".//textarea[@id='post-body']"
    CREATED_BODY_TEXT_XPATH = ".//p[text()=‘{post.body}’]"
    CREATE_POST_BUTTON_XPATH = ".//button[@class='btn btn-primary']"
    UPDATE_POST_BUTTON_XPATH = './/button[text()="Save Updates"]'
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
    UNIQUE_POST_CHECKBOX_XPATH = './/input[@type="checkbox"]'
    UNIQUE_CREATED_CHECKBOX_XPATH = ".//p[text()='Is this post unique? : yes']"
    UNIQUE_CHECKBOX_POSITIVE_TEXT = 'Is this post unique? : yes'
    OPTIONS_XPATH = './/select[@id="select1"]'
    VISIBILITY_SELECTION_XPATH = ".//option[@value='{option}']"
    CREATED_OPTION_XPATH = './/u'
    CREATED_OPTION_ALL_USERS_TEXT = 'All Users'
    OPTION_ALL_USERS = './/option[@value="All Users"]'
    OPTION_ALL_USERS_TEXT = 'All Users'
    OPTION_PRIVATE_MESSAGE = './/option[@value="One Person"]'
    OPTION_PRIVATE_MESSAGE_TEXT = 'One Person'
    OPTION_GROUP_MESSAGE = './/option[@value="Group Person"]'
    OPTION_GROUP_MESSAGE_TEXT = 'Group Person'
