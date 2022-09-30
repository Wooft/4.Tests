import unittest

import main
from main import get_doc_owner_name
from unittest.mock import MagicMock
from unittest.mock import patch

def get_input(text):
    return input(text)

# class TestFumction(unittest.TestCase):
#     def setUp(self) -> None:
#         print('setUP ===>')
#
#     def tearDown(self) -> None:
#         print('tearDown ===>')
#
#     @patch(main.get_doc_owner_name(), return_value='11-2')
#     def test_get_doc_owner_name(self, input):
#         etalon = 0
#         result = get_doc_owner_name()

class Test(unittest.TestCase):

    @patch('builtins.input', return_value='yes')
    def test_answer_yes(self, mock_input):
        self.assertEqual('you entered yes')
