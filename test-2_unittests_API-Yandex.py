# Задание №2
# unit-tests
# Автотест API Яндекса
# python -m unittest -v test-2_unittests_API-Yandex.py


import unittest
from parameterized import parameterized, parameterized_class
from mock import patch, MagicMock
import lets_use_API_Yandex


class APIYandexTest(unittest.TestCase):
    @parameterized.expand([('http://httpbin.org/get', 200), ])
    def test_request(self, url, expected_status):
        sut = lets_use_API_Yandex.check_request
        actual_status = sut()
        self.assertEqual(expected_status, actual_status)


if __name__ == '__main__':
    unittest.main()
