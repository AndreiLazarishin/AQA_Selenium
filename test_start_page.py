import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

log = logging.getLogger(__name__)


class TestStartPage:

    def test_empty_email_alert(self):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the email field
            Clear the email field
            Check the email-field alert message
        """
        driver = webdriver.Chrome(r"C:\Users\andrii.lazaryshyn\PycharmProjects\AQA_Selenium\chromedriver.exe")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        log.info('Starting test - check email field alert')
        email = driver.find_element(by=By.XPATH, value='.//*[@name="email" and @placeholder="you@example.com"]')
        email.send_keys('villy@wonka.com')
        sleep(2)
        email.clear()
        sleep(5)
        alert_message = driver.find_element(by=By.XPATH, value='.//*[text()="You must provide a valid email address."]')
        assert alert_message.is_displayed()
        log.info('Test passed. Alert is displayed')
        driver.close()

    def test_empty_password_alert(self):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the password field
            Clear the password field
            Check the password-field alert message
        """
        driver = webdriver.Chrome(r"C:\Users\andrii.lazaryshyn\PycharmProjects\AQA_Selenium\chromedriver.exe")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        log.debug('Starting test - check the password field alert')
        password = driver.find_element(by=By.XPATH, value='.//*[@name="password" and @placeholder="Create a password"]')
        password.send_keys('Icht|@ndr')
        sleep(2)
        password.clear()
        sleep(5)
        alert_message = driver.find_element(by=By.XPATH,
                                            value='.//*[text()="Password must be at least 12 characters."]')
        assert alert_message.is_displayed()
        log.debug('Test passed. Alert is displayed')

        driver.close()

    def test_incorrect_login(self):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the username & password fields with random value
            Click on the 'Sign in' button
            Check the invalid username\password alert message
        """
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\andrii.lazaryshyn\PycharmProjects\AQA_Selenium\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        log.warning('Invalid logging test scenario started')
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.send_keys('User1')

        passwd = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        passwd.send_keys('Kavabanga')

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()

        sleep(10)

        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"
        log.warning('Test passed. Only authorized users can log in')

        # Close driver
        driver.close()

    def test_empty_login(self):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Clear the username & password fields
            Click on the 'Sign in' button
            Check the invalid username\password alert message
        """
        driver1 = webdriver.Chrome(r"C:\Users\andrii.lazaryshyn\PycharmProjects\AQA_Selenium\chromedriver.exe")
        driver1.get("https://qa-complex-app-for-testing.herokuapp.com/")

        username = driver1.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.clear()

        password = driver1.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()

        button = driver1.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()

        sleep(5)

        error_element = driver1.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        driver1.close()

    def test_success_login(self):
        """
        Setup:
            Open the qa-complex site
        Steps:
            Fill in the username field
            Clear the password field
            Click on the 'Log in' button
            Check if there is a 'Chat' button
        """
        driver = webdriver.Chrome(r"C:\Users\andrii.lazaryshyn\PycharmProjects\AQA_Selenium\chromedriver.exe")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        log.info('Successful log in test started')
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.send_keys('abdul')
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys('Ci6aZ9khFDWu38L')
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(3)

        chat_button = driver.find_element(by=By.XPATH, value='.//*[@title="" and @data-original-title="Chat"]')
        assert chat_button.is_displayed()
        log.info('Test passed. Authorized users can log in the app.')

        driver.close()
