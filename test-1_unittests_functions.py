# Задание №1
# unit-tests
# по Д/З к лекции «Функции — использование встроенных и создание собственных» (py-basic_task)
# python -m unittest -v test-1_unittests_functions.py

import unittest
from parameterized import parameterized, parameterized_class
from mock import patch, MagicMock
import py_basic_task


@parameterized_class(('docs', 'dirs'),
                     [(
                             [  # docs:
                                 {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                                 {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                                 {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}],
                             {  # dirs:
                                 '1': ['2207 876234', '11-2'],
                                 '2': ['10006'],
                                 '3': []}
                     ), ])
class CorrectiveActionsTestClass(unittest.TestCase):
    @patch('py_basic_task.get_data', MagicMock(return_value='unittest'))
    def test_get_new_doc(self):
        sut = py_basic_task.get_new_doc
        actual_doc = sut()
        self.assertIsInstance(actual_doc, dict, 'Ошибка создания нового документа!!!')
        self.assertEqual({"type": 'unittest', "number": 'unittest', "name": 'unittest'}, actual_doc,
                         'Ошибка создания нового документа!!!')

    @patch('py_basic_task.get_data', MagicMock(return_value='unittest'))
    def test_add_docs(self):
        expected_doc = {"type": 'unittest', "number": 'unittest', "name": 'unittest'}
        expected_shelf = '1'
        sut = py_basic_task.add_docs
        actual_doc = sut(self.docs, self.dirs)
        self.assertEqual(expected_doc, actual_doc['new_doc'],
                         'Ошибка добавления нового документа!!!')
        self.assertEqual(expected_shelf, actual_doc['new_shelf'],
                         'Ошибка добавления нового документа на полку!!!')

    @parameterized.expand([({"type": 'unittest', "number": 'unittest', "name": 'unittest'}, '1')])
    def put_doc_on_shelf(self, doc, shelf):
        sut = py_basic_task.put_doc_on_shelf
        actual_shelf = sut(self.dirs, doc, shelf)
        self.assertEqual(shelf, actual_shelf)


@parameterized_class(('docs', 'dirs'),
                     [(
                             [  # docs:
                                 {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                                 {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                                 {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}],
                             {  # dirs:
                                 '1': ['2207 876234', '11-2'],
                                 '2': ['10006'],
                                 '3': []}
                     ), ])
class SelectiveActionsTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # print("method setUpClass")
        pass

    def setUp(self):
        # print("method setUp")
        pass

    @parameterized.expand([
        ('11-2', {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}),
        ('None', None)])
    def test_get_person_by_doc(self, doc_num, expected_person):
        sut = py_basic_task.get_person
        actual_shelf = sut(self.docs, doc_num)
        self.assertEqual(expected_person, actual_shelf,
                         'Ошибка поиска документа по его номеру!!!')

    @parameterized.expand([
        ('11-2', {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}),
        ('None', None)])
    def test_show_person(self, doc_num, expected_person):
        sut = py_basic_task.show_person
        with patch('py_basic_task.get_data') as get_data_mock:
            get_data_mock.return_value = '11-2'
        actual_person = sut(self.docs, self.dirs, doc_num)
        self.assertEqual(expected_person, actual_person,
                         'Ошибка поиска документа по его номеру!!!!!!')

    @parameterized.expand([('11-2', '1'), ('22-1', '')])
    def test_get_shelf_for_doc(self, doc_num, expected_shelf):
        sut = py_basic_task.get_shelf_for_doc
        actual_person = sut(self.dirs, doc_num)
        self.assertEqual(expected_shelf, actual_person,
                         'Ошибка поиска расположения документа по его номеру!!!')

    @parameterized.expand([('11-2', '1'), ('22-1', '')])
    def test_show_shelf_for_doc(self, doc_num, expected_shelf):
        sut = py_basic_task.show_shelf_for_doc
        with patch('py_basic_task.get_data') as get_data_mock:
            get_data_mock.return_value = '11-2'
        actual_shelf = sut(self.docs, self.dirs, doc_num)
        self.assertEqual(expected_shelf, actual_shelf,
                         'Ошибка поиска расположения документа по его номеру!!!')

    @parameterized.expand([
        ({"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
         '"invoice" "11-2" "Геннадий Покемонов"'),
    ])
    def test_get_document_to_line(self, doc, expected_info_line):
        sut = py_basic_task.get_document_to_line
        actual_info_line = sut(doc)
        self.assertEqual(expected_info_line, actual_info_line,
                         'Ошибка конструктора выдачи документа в одну строку!!!')

    # @parameterized.expand([
    #     (['"passport" "2207 876234" "Василий Гупкин"',
    #       '"invoice" "11-2" "Геннадий Покемонов"',
    #       '"insurance" "10006" "Аристарх Павлов"']),
    # ])
    # def test_show_list_documents(self, expected_doc_list):
    #     sut = py_basic_task.show_list_documents
    #     actual_doc_list = sut(self.docs)
    #     self.assertEqual(expected_doc_list, actual_doc_list,
    #                      'Ошибка выдачи списка документов!!!')

    @parameterized.expand([('1', ['"passport" "2207 876234" "Василий Гупкин"',
                                  '"invoice" "11-2" "Геннадий Покемонов"']),
                           ('3', []),
                           ('4', []), ])
    def test_show_docs_on_shelf(self, shelf_num, expected_docs):
        sut = py_basic_task.show_docs_on_shelf
        actual_docs = sut(self.docs, self.dirs, shelf_num)
        self.assertEqual(expected_docs, actual_docs,
                         'Ошибка выдачи списка документов!!!')


class TestsCapabilitiesOfShow(unittest.TestCase):
    def test_show_result(self):
        sut = py_basic_task.show_result
        expected_value = 'Заголовок: есть результат! Есть замечание. Есть дополнения.'
        actual_value = sut('есть результат!', 'Заголовок:', 'Есть замечание.', 'Есть дополнения.')
        self.assertEqual(expected_value, actual_value, 'Ошибка печати результатов!!!')


if __name__ == '__main__':
    unittest.main()
