#

from pprint import pprint


def display_response(url, my_request, response):
    print(my_request.upper(), url, end=':\t')
    print('success' if response.status_code == 200 else 'fail', end='!\t')
    pprint(response)
