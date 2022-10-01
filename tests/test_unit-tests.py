import unittest
from unittest.mock import patch
from unittest import mock
from parameterized import parameterized
from main import get_doc_owner_name, get_all_doc_owners_names, show_all_docs_info, get_doc_shelf, add_new_doc, delete_doc, add_new_shelf
from ya_di import create_folder, delete_folder

class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=['2207 876234', '11-2', '10006'])
    def test1_get_doc_owner_name(self, mock_input):
        result_1 = get_doc_owner_name()
        result_2 = get_doc_owner_name()
        result_3 = get_doc_owner_name()
        self.assertTrue(result_1 == 'Василий Гупкин' and result_2 == 'Геннадий Покемонов' and result_3 == 'Аристарх Павлов')

    def test2_get_all_doc_owners_names(self):
        etalon = { 'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}
        res = get_all_doc_owners_names()
        self.assertEqual(etalon, res)

    def test3_show_all_docs_info(self):
        etalon = ['passport "2207 876234" "Василий Гупкин"',
                  'invoice "11-2" "Геннадий Покемонов"',
                  'insurance "10006" "Аристарх Павлов"']
        res = show_all_docs_info()
        self.assertEqual(res, etalon)
    @patch ('builtins.input', side_effect=['2207 876234', '11-2', '10006'])
    def test4_get_doc_shelf(self, mock_input):
        res_1 = get_doc_shelf()
        res_2 = get_doc_shelf()
        res_3 = get_doc_shelf()
        self.assertTrue(res_1 == '1' and res_2 == '1' and res_3 == '2')

    string_of_ints = ['112', 'Passport', 'Акакий', 2]

    def test5_add_new_doc(self):
        mock_args = ['112', 'Passport', 'Акакий', 2]
        etalon = 2
        with mock.patch('builtins.input', side_effect=mock_args):
            res = add_new_doc()
        self.assertEqual(res, etalon)

    @patch ('builtins.input', side_effect=['2207 876234', '11-2', '10006'])
    def test6_delete_doc(self, mock_input):
        res_1 = delete_doc()
        res_2 = delete_doc()
        res_3 = delete_doc()
        self.assertTrue(res_1 == ('2207 876234', True) and res_2 == ('11-2', True) and res_3 == ('10006', True))

    @patch ('builtins.input', side_effect=['1', '2', '4', '5'])
    def test7_add_new_shelf(self, mock_input):
        res_1 = add_new_shelf()
        res_2 = add_new_shelf()
        res_3 = add_new_shelf()
        res_4 = add_new_shelf()
        self.assertTrue(res_1 == ('1', False) and res_2 == ('2', False) and  res_3 == ('4', True) and res_4 == ('5', True))

class test_yandex(unittest.TestCase):
    @parameterized.expand(
        [
            ('Новая папка', 201),
            ('Старая папка', 201),
            ('Новая папка', 409)
        ]
    )
    def test_create_folder(self, input, output):
        result = create_folder(input)
        self.assertEqual(output, result)

    @parameterized.expand(
        [
            ('Новая папка', 204),
            ('Старая папка', 204),
            ('Новая папка', 404)
        ]
    )
    def test_delete_folder(self, input, output):
        result = delete_folder(input)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
