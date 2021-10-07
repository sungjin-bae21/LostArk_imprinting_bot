"""
    TDD 를 위한 unittest
"""

import unittest
from message_parser import MessageParser

class MyTest(unittest.TestCase):
    def test(self):
        parser = MessageParser()
        data = parser.parse_first_bonus_book_to_data("123")
        self.assertEqual(1,0)


unittest.main()