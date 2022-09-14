import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


# - Створити тест на реєстрацію.
# Нюанс номер 1:
# Тест має проходити більше 1 разу, тобто данні в полях мають бути повністю або частково випадковими
# (Оскільки той самий юзер не може бути зареєстрований двічі)
# Нюанс номер 2:
# Вам потрібно самостійно придумати перевірку, що буде підверджувати успішність реєстрації.
# Це може бути перевірка наявності якогось поля, його значення, повідомлення або первірка URL.
# class Generate_random:
#     def rand_pass(self, length):
#         generate_pass = ''.join([random.choice(string.ascii_lowercase + string.digits) for i in range(length)])
#         return generate_pass
#
#     def random_email(self, dog):
#         generate_email = ''.join([random.choice(string.ascii_lowercase) for e in range(dog)]) + '@john.com'
#         return generate_email
#
#     def rand_username(self, name):
#         generate_name = ''.join([random.choice(string.ascii_lowercase) for n in range(name)])
#         return generate_name


class TestRegistration:

    def rand_pass(self, length):
        generate_pass = ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(length)])
        return generate_pass

    def random_email(self, dog):
        generate_email = ''.join([random.choice(string.ascii_lowercase) for _ in range(dog)]) + '@john.com'
        return generate_email

    def rand_username(self, name):
        generate_name = ''.join([random.choice(string.ascii_lowercase) for _ in range(name)])
        return generate_name

    def test_registration(self):
        driver = webdriver.Chrome(r"C:\Users\andrii.lazaryshyn\PycharmProjects\AQA_Selenium\chromedriver.exe")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        name = driver.find_element(by=By.XPATH, value='.//*[@name="username" and @placeholder="Pick a username"]')
        name.send_keys(self.rand_username(6))
        print(self.rand_username(6))
        sleep(1)

        mailo = driver.find_element(by=By.XPATH, value='.//*[@name="email" and @placeholder="you@example.com"]')
        mailo.send_keys(self.random_email(7))
        print(self.random_email(7))
        sleep(1)

        pastor = driver.find_element(by=By.XPATH, value='.//input[@name="password" and @class="form-control"]')
        pastor.send_keys(self.rand_pass(13))
        print(self.rand_pass(13))
        sleep(1)

        button = driver.find_element(by=By.XPATH, value='.//*[text()="Sign up for OurApp"]')
        button.click()
        sleep(1)

        error_element = driver.find_element(by=By.XPATH, value='.//strong')
        assert error_element.is_displayed()

        driver.close()
