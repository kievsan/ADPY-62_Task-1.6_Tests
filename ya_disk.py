# Примеры кода к лекции 3.1
# "Request"
# https://github.com/kievsan/PY-62_3.1.requestsPy_code.git


from pprint import pprint
import requests
from Tools import display_response


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self, params={}):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        # response = requests.get(files_url, headers=headers)
        response = requests.get(files_url, headers=headers, params=params, files={})
        return response

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def create_directory_on_disk(self, disk_dir_path):
        create_dir_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": disk_dir_path, "overwrite": "true"}
        response = requests.put(create_dir_url, headers=headers, params=params)
        display_response(create_dir_url, 'PUT', response)
        pprint(response.headers)
        pprint(response.json())
        return response

    def has_file(self, my_file):
        return False

    def has_dir(self, my_dir):
        return