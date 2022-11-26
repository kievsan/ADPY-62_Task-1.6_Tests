# ADPY-62
# Домашнее задание к лекции «Разработка тестов»

from py_basic_task import main_menu
from lets_use_API_Yandex_Disk import check_requests
from lets_use_API_Yandex_Disk import create_ya_dir


if __name__ == '__main__':
    start_check_API = 1
    if start_check_API:
        response_ya_status = check_requests(url='http://yandex.ru')
        has_ya_dir = create_ya_dir('Test')

    else:
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        directories = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }
        main_menu(documents, directories)
