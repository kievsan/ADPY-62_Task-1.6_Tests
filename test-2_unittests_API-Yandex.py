# Задание №2
# unit-tests
# Автотест API Яндекса
# python -m unittest -v test-2_unittests_API-Yandex.py


import unittest
from parameterized import parameterized, parameterized_class
from mock import patch, MagicMock
import lets_use_API_Yandex


class APIYandexTest(unittest.TestCase):
    @parameterized.expand([('http://httpbin.org/get', 'get', 2),
                           ('http://yandex.ru', 'get', 2),
                           ('http://yandex.ru/get', 'get', 2), ])
    def test_request(self, url, request, expected_status):
        sut = lets_use_API_Yandex.check_requests
        actual_status = int(sut(url, request)/100)
        self.assertEqual(expected_status, actual_status,
                         f'Ошибка выполнения запроса!')


if __name__ == '__main__':
    unittest.main()
