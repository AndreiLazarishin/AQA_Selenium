import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


@pytest.fixture(scope='function')
def start_page():
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(BASE_URL)
    driver.implicitly_wait(1.5)
    yield StartPage(driver)
    driver.close()


@pytest.fixture()
def random_user():
    user = User()
    user.fill_data()
    return user


@pytest.fixture()
def known_user():
    user = User()
    user.username = 'abdul'
    user.password = 'Ci6aZ9khFDWu38L'
    return user


@pytest.fixture()
def hello_page(start_page, random_user):
    """Sign up as a user and return the page"""
    return start_page.sign_up_and_verify(random_user)


@pytest.fixture()
def known_profile(hello_page):
    """Find a user and open its page"""
    search = hello_page.header.open_search()
    search.find_profile()
    return search
