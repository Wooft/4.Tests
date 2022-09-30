import unittest
from unittest.mock import patch
from main import get_doc_owner_name

class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=['2207 876234', '11-2', '10006'])
    def test_get_doc_owner_name(self, mock_input):
        result_1 = get_doc_owner_name()
        result_2 = get_doc_owner_name()
        result_3 = get_doc_owner_name()
        self.assertTrue(result_1 == 'Василий Гупкин' and result_2 == 'Геннадий Покемонов' and result_3 == 'Аристарх Павлов')



    # @patch('builtins.input', side_effect=['First', 'Second', 'Third'])
    # def test_using_side_effect(self, mock_input):
    #     calling_1 = mock_input()
    #     calling_2 = mock_input()
    #     calling_3 = mock_input()
    #     self.assertTrue(calling_1 == 'First' and calling_2 == 'Second' and
    #                     calling_3 == 'Third')