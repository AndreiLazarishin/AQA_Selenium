import logging


class TestSearchPage:
    log = logging.getLogger("[ChatPage]")

    def test_find_profile(self, hello_page):
        """Find the profile"""
        search = hello_page.header.open_search()
        search.find_profile()

    def test_follow_the_profile(self):
        """Follow the profile"""
