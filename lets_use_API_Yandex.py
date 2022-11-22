#


import requests
from pprint import pprint


def main_for_API_Yandex():
    check_request()


def check_request(url='http://httpbin.org/get'):
    response = requests.get(url)
    res = response.status_code
    pprint(response)
    if res == 200:
        print('Проблем с подключением нет!')
    elif res >= 400:
        print('Точно какие-то проблемы с подключением нет!')
    return res
