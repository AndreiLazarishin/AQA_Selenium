import logging

from pages.utils import rand_str, log_decorator


class TestChat:
    log = logging.getLogger("[ChatPage]")

    @log_decorator
    def test_chat(self, hello_page):
        """
            Set up:
                Sign-up\Sign-in as a user
            Steps:
                Open chat
                Send message
                Verify message
                Send one more message
                Verify messages
                """
        chat = hello_page.header.open_chat()
        message_1 = rand_str(10)
        chat.send_message(message_1)
        chat.verify_messages([message_1])
        message_2 = rand_str(14)
        chat.send_message(message_2)
        chat.verify_messages([message_1, message_2])
