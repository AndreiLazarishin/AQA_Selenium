from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_incorrect_login(self):
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\andrii.lazaryshyn\PycharmProjects\AQA_Selenium\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        username.send_keys('User1')

        passwd = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        passwd.send_keys('Kavabanga')

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()

        sleep(10)

        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    def test_empty_login(self):
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
