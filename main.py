from pprint import pprint

print('Задание №1')

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

# Получение списка документов
def list_of_doc(documents: dict) -> list:
    list_doc = []
    for item in documents:
        list_doc.append(item['number'])
    return list_doc

def people(documents: dict) -> str:
    list_of_doc(documents)
    print("Cписок существующих документов: ")
    print(list_of_doc(documents))

    inname = input(f'Введите номер документа: ')
    if inname in list_of_doc(documents):
        for element in documents:
            if element['number'] == inname:
                return (f"{element['name']} \n")
    else:
        return "Введено неверное значение, повторите попытку!"

def shelf(directories: dict) -> int:
    print("Cписок существующих документов: ")
    print(list_of_doc(documents))
    while True:
        try:
            num = input('Введите номер документа:')
            if num in list_of_doc(documents):
                for key, item in directories.items():
                    if num in item:
                        return key
                break
        except Exception as e:
            print('Данные введены неверно, попробуйте снова!')

def list(documents: dict) -> list:
    list_documents = []
    for elements in documents:
        list_documents.append(f"{elements['type']} {elements['number']} {elements['name']}")
    return list_documents

def add(documents: dict, directories: dict) -> dict:
    new_dict = {}
    num_doc = input('Введите номер документа: ')
    new_dict['type'] = input('Введите тип: ')
    new_dict['number'] = num_doc
    new_dict['name'] = input('Введите имя: ')
    documents.append(new_dict)
    print()
    print("Данные добавлены в список: ")
    print(list(documents))

    while True:
        try:
            new = input('Введите номер полки: ')
            if new in directories.keys():
                for keys, values in directories.items():
                    if keys == new:
                        values.append(num_doc)
                return directories
        except Exception as e:
            print('Данные введены неверно, попробуйте снова!')

def delete(documents: dict, directories: dict):
    print("Cписок существующих документов: ")
    pprint(documents)
    num_d = input(f'Введите номер документа: ')
    if num_d in list_of_doc(documents):
        for element in documents:
            if element['number'] == num_d:
                documents.remove(element)
        for keys, elements in directories.items():
            if num_d in elements:
                elements.remove(num_d)
        return 'Документ был успешно удален'
    else:
        print('Данного документа не существует, проверьте данные!')


def move(directories):
    print("Cписок существующих документов: ")
    print(list_of_doc(documents))
    num_d = input('Введите номер документа: ')
    num_p = input('Введите номер полки: ')
    list_of_shelf = []
    list_of_shelf.append(directories.keys())
    if num_d in list_of_doc(documents):
        if num_p in directories.keys():
            for keys, values in directories.items():
                if num_d in values:
                    values.remove(num_d)
            for keys, values in directories.items():
                if keys == num_p:
                    if values.count(num_d) == 0:
                        values.append(num_d)
                    else:
                        print('Документ уже лежит на полке')
        else:
            pass
    else:
        pass
    print(directories)


def add_shelf(directories):
    num_p = input('Введите номер новой полки (необходимо ввести число): ')
    if num_p.isnumeric() == True:
        if num_p in directories.keys():
            print('Полка уже существует! \n')
        else:
            directories.setdefault(num_p, [])
            print(directories)
    else:
        pass


while True:
    command = input("Введите команду для выбора действия: \n q - Выход \n p - показать владельца по немеру документа "
                    "\n s - показать на какой полке лежит документ \n l - вывести список документов \n a - добавить "
                    "новый документ \n d - удалить документ по номеру \n m - переместить документ с полки на полку \n "
                    "as - добавить новую полку \n Введите команду: ")
    if command == 'p':
        pprint(people(documents))
    if command == 's':
        pprint(f'Документ лежит на полке № {shelf(directories)}')
    if command == 'l':
        pprint(documents)
    if command == 'a':
        pprint(f"Документ добавлен на полку: \n {add(documents, directories)}")
    if command == 'd':
        pprint(delete(documents, directories))
    if command == 'm':
        move(directories)
    if command == 'as':
        add_shelf(directories)
    if command == 'q':
        print('Завершение работы')
        break
