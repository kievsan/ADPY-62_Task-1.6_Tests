#


import requests
from pprint import pprint


def main_for_API_Yandex(url='http://yandex.ru', request='get'):
    response_status = check_requests(url, request)
    return response_status


def check_requests(url='http://httpbin.org/get', request='get'):

    if request == 'get':
        response = requests.get(url)
    elif request == 'post':
        response = requests.post(url)
    else:
        return 0
    status = response.status_code
    print(request.upper(), url, end=':\t')
    pprint(response)
    return status
