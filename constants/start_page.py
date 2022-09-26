class StartPageConstants:
    # Sign in
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"
    SIGN_IN_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_LOGIN_ERROR_TEXT = "Invalid username / pasword"

    # Sign up
    SIGN_UP_USERNAME_FIELD_XPATH = './/*[@name="username" and @placeholder="Pick a username"]'
    SIGN_UP_EMAIL_FIELD_XPATH = './/*[@name="email" and @placeholder="you@example.com"]'
    SIGN_UP_PASSWORD_FIELD_XPATH = './/input[@name="password" and @class="form-control"]'
    SIGN_UP_BUTTON_XPATH = './/*[text()="Sign up for OurApp"]'
    SIGN_UP_EMAIL_ERROR_TEXT = 'You must provide a valid email address.'
    SIGN_UP_EMAIL_ERROR_XPATH = './/div[@class="alert alert-danger small liveValidateMessage ' \
                                'liveValidateMessage--visible"] '
    SIGN_UP_PASSWORD_ERROR_TEXT = 'Password must be at least 12 characters.'
    SIGN_UP_PASSWORD_ERROR_XPATH = './/div[@class="alert alert-danger small liveValidateMessage ' \
                                   'liveValidateMessage--visible"] '
    SIGN_UP_USERNAME_ERROR_TEXT = 'Username must be at least 3 characters.'
    SIGN_UP_USERNAME_ERROR_XPATH = './/div[@class="alert alert-danger small liveValidateMessage ' \
                                   'liveValidateMessage--visible"] '
