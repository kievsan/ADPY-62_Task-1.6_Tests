# PY-62
# Домашнее задание к лекции «Функции — использование встроенных и создание собственных»
# (https://github.com/netology-code/py-homework-basic)
#  реализовать пользовательские команды
#  p – people, s – shelf, l– list, ls - list shelf, a – add, d – delete, m – move, as – add shelf

def main_menu(doc_list, shelf_dict):
    while True:
        command = input("\nEnter the command (q - quit): ").strip().lower()
        if not command:
            show_result("\t No command!")
        elif command == "q" or command == "й":
            show_result("The program is completed!")
            break
        elif command == "p" or command == "з":
            show_result("Операция 'people'. Имя владельца документа по его номеру:")
            show_person(doc_list, shelf_dict, get_data("Введите номер искомого документа: "))
        elif command == "s" or command == "ы":
            show_result("Операция 'shelf'. На какой полке находится документ:")
            show_shelf_for_doc(doc_list, shelf_dict, get_data("Введите номер искомого документа: "))
        elif command == "l" or command == "д":
            show_result("Операция 'list'. Список документов:")
            show_list_documents(doc_list)
        elif command == "ls" or command == "ды":
            show_result("Операция 'list shelf'. Список документов на кокретной полке:")
            show_docs_on_shelf(doc_list, shelf_dict, get_data("Введите номер запрашиваемой полки: "))
        elif command == "a" or command == "ф":
            show_result("Операция 'add'. Добавим новый документ в список и на полку:")
            add_docs(doc_list, shelf_dict)
        elif command == "d" or command == "в":
            show_result("Операция 'delete'. Удалим документ из списка и уберём с полки:")
            delete_doc(doc_list, shelf_dict, get_data("Введите номер удаляемого документа: "))
        elif command == "m" or command == "ь":
            show_result("Операция 'move'. Переместим документ с полки на полку:")
            move_doc(doc_list, shelf_dict)
        elif command == "as" or command == "фы":
            show_result("Операция 'add shelf'. Добавим новую полку:")
            add_shelf(shelf_dict, get_data("Введите номер добавляемой полки: "))
        else:
            show_result("\t Unknown command!")


def show_result(result, title="", comment1="", comment2=""):
    msg = f'{title} {result} {comment1} {comment2}'.strip()
    print(msg)
    return msg


def get_data(get_me_data):
    """
    Ввод строки с консоли
    :param get_me_data: str описание вводимых данных
    :return: str
    """
    data = ""
    while not data:
        data = input(get_me_data).strip()
    return data


def show_person(docs, shelfs, doc_number):
    if doc_number:
        result = get_person(docs, doc_number)
    else:
        result = get_person(docs, get_data("Введите номер искомого документа: "))
    if result:
        show_result(result["name"], " Владелец документа -")
        show_shelf_for_doc(docs, shelfs, doc_number)
    else:
        show_result("Документ с таким номером не найден!")
    return result


def get_person(docs, doc_number='11-2'):
    """
    Найти данные владельца по номеру документа
    :param docs: [{...}, ... , {...}] список словарей (документов)
    :param doc_number: str, номер докумета
    :return: {}, данные документа, найденные по номеру докумета
    """
    if doc_number:
        for doc in docs:
            if str(doc["number"]).strip().upper() == str(doc_number).strip().upper():
                return doc
    return None


def show_shelf_for_doc(docs, shelfs, doc_number=""):
    if doc_number:
        result = get_shelf_for_doc(shelfs, doc_number)
    else:
        result = get_shelf_for_doc(shelfs, get_data("Введите номер искомого документа: "))
    if result:
        show_result(result, " Документ найден на", "полке")
        show_result(get_document_to_line(get_person(docs, doc_number)))
    else:
        show_result("Документ не найден!")
    return result


def get_shelf_for_doc(shelfs, doc_number):
    """
    Найти номер полки по номеру документа
    :param shelfs: словарь полок со списками номеров документов
    :param doc_number: str номер документа
    :return: str номер полки
    """
    for shelf, list_numbers in shelfs.items():
        if doc_number in list_numbers:
            return shelf
    return ""


def show_list_documents(docs):
    """
    выводит в консоль список всех документов
    :param docs: [{...}, ... , {...}] список словарей (документов)
    :return: None
    """
    doc_list = []
    for doc in docs:
        doc_to_line = get_document_to_line(doc)
        doc_list.append(doc_to_line)
        show_result(doc_to_line)
    return doc_list


def get_document_to_line(doc):
    """
    Вернёт конкретный документ в одну строку
    :param doc: {...} документ
    :return: str документ
    """
    person = ""
    for data in doc.values():
        person += ' "' + data + '"'
    return person.strip()


def show_docs_on_shelf(docs, shelfs, shelf):
    """
    выводит в консоль список документов на конкретной полке
    :param docs: [{...}, ... , {...}] список словарей (документов)
    :param shelfs: {key: [...], ...} словарь полок со списками номеров документов,
                                     ключи - номера полок
    :param shelf: str номер полки
    :return: doc_list: []
    """
    doc_list = []
    if not (shelf in shelfs):
        show_result("Нет полки с таким номером!")
        return doc_list
    numbers = shelfs[shelf]
    if not numbers:
        show_result("Полка пустая!")
    else:
        for doc_number in numbers:
            doc_to_line = get_document_to_line(get_person(docs, doc_number))
            doc_list.append(doc_to_line)
            show_result(doc_to_line)
    return doc_list


def add_docs(doc_list, shelf_dict):
    new_doc = get_new_doc()
    new_shelf = get_data("Введите номер полки для нового документа: ")
    doc_list.append(new_doc)
    while not put_doc_on_shelf(shelf_dict, new_doc, new_shelf):
        show_result(f'"{new_shelf}":\t"Нет такой полки!')
        new_shelf = '1'
        show_result(f'Положим на полку "{new_shelf}"')
    show_result(get_document_to_line(new_doc), " Добавлен новый документ", "на указанную полку")
    return {'new_doc': new_doc, 'new_shelf': new_shelf}


def get_new_doc():
    data = {"type": get_data("Введите тип нового документа: "),
            "number": get_data("Введите номер нового документа: "),
            "name": get_data("Введите имя и фамилию владельца нового документа: ")}
    return data


def put_doc_on_shelf(shelfs, doc, shelf):
    """
    Кладёт документ на полку
    :param shelfs: {key: [...], ...} словарь полок со списками номеров документов,
                                     ключи - номера полок
    :param doc: {...} документ
    :param shelf: str номер полки
    :return: None
    """
    if shelf in shelfs:
        shelfs[shelf].append(doc["number"])
        return shelf
    return ""


def delete_doc(docs, shelfs, doc_number=""):
    doc_number = doc_number.strip()
    if not doc_number:
        doc_number = get_data("Введите номер удаляемого документа: ")
    doc_number = doc_number.strip()
    result = delete_doc_from_docs(docs, doc_number)
    if result:
        show_result(get_document_to_line(result), " Документ", "удалён из списка документов")
    else:
        show_result("Документ с таким номером не найден в списке документов!")
    result = delete_doc_from_shelfs(shelfs, doc_number)
    if result:
        show_result(result, " Документ убрали с", "полки")
    else:
        show_result("Документа нет на полках!")


def delete_doc_from_shelfs(shelfs, doc_number):
    """
    Убирает документ с полки
    :param shelfs: {key: [...], ...} словарь полок со списками номеров документов,
                                     ключи - номера полок
    :param doc_number: str номер документа
    :return: str номер полки
    """
    for shelf in shelfs:
        numbers = shelfs[shelf]
        if doc_number in numbers:
            numbers.remove(doc_number)
            return shelf
    return ""


def delete_doc_from_docs(docs, doc_number):
    """
    Удаляет документ из списка документов
    :param docs: [{...}, ... , {...}] список словарей (документов)
    :param doc_number: str номер документа
    :return: {...} документ
    """
    for doc in docs:
        if doc["number"] == doc_number:
            docs.remove(doc)
            return doc
    return {}


def move_doc(docs, shelfs, doc_number="", new_shelf=""):
    if len(shelfs) < 2:
        show_result("Недостаточно полок для проведения операции!")
    doc = get_person(docs, doc_number)
    if not doc:
        while True:
            doc = get_person(docs, get_data("Введите номер документа: "))
            if doc:
                show_result(get_document_to_line(doc))
                break
            show_result("Документ не найден!")
    doc_number = doc["number"]
    doc_shelf = get_shelf_for_doc(shelfs, doc_number)
    if not (new_shelf in shelfs) or new_shelf == doc_shelf:
        while True:
            new_shelf = get_data("Введите номер полки для выбранного документа: ")
            if (new_shelf in shelfs) and not (new_shelf == doc_shelf):
                break
            if new_shelf in shelfs:
                show_result("Выбрана эта же полка! Операция отменена")
            else:
                show_result("Полка не найдена!")
    shelf = delete_doc_from_shelfs(shelfs, doc_number)
    new_shelf = put_doc_on_shelf(shelfs, doc, new_shelf)
    show_result(shelf, " Документ переместили с полки", "на полку", new_shelf)


def add_shelf(shelfs, shelf_number=""):
    if not shelf_number:
        shelf_number = get_data("Введите номер добавляемой полки: ")
    if shelf_number in shelfs:
        show_result("Полка с таким номером уже есть!")
        return False
    shelfs[shelf_number] = list()
    show_result(shelf_number, " Добавлена полка:")
    return True
