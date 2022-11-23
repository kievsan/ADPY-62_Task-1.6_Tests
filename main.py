# ADPY-62
# Домашнее задание к лекции «Разработка тестов»

from py_basic_task import main_menu
from lets_use_API_Yandex import main_for_API_Yandex


if __name__ == '__main__':
    start_check_API = 1
    if start_check_API:
        main_for_API_Yandex('http://yandex.ru')
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
