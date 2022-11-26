#


from pprint import pprint
import requests
from ya_disk import YandexDisk
from Tools import display_response


YA = YandexDisk(token='')


def create_ya_dir(disk_dir_path):
    dir_response = YA.create_directory_on_disk(disk_dir_path)
    ya_files = YA.get_files_list()
    ya_files_list = [{'path': file['name'],
                      'type': file['type'],
                      'date': file['created']}
                     for file in ya_files.json()['items'] if 'type' == 'dir']
    pprint(ya_files_list)
    return YA.has_file(disk_dir_path)


def check_requests(url='http://httpbin.org/get'):
    response = requests.get(url)
    status = response.status_code
    display_response(url, 'GET', response)
    pprint(response.headers)
    return status
