import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def is_exists(self, xpath, by=By.XPATH):
        """Check that element exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return True
        except selenium.common.exception.NoSuchElementException:
            return False

    def fill_field(self, xpath, value):
        """Fill, Clear and fill fields"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Find and click"""
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def get_element_text(self, xpath):
        """Find element and get text"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element.text

    def fill_and_clear(self, xpath, value):
        """Fill the field and clear it after"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.send_keys(value)
        element.clear()
