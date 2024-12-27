def filter_by_state(list_dictionaries: list, state: str) -> list:
    """
    Функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    # Выход функции со статусом по умолчанию 'EXECUTED'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    # Выход функции, если вторым аргументов передано 'CANCELED'
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    """
    output_list = []
    for dict in list_dictionaries:
        # if dict["state"] != state:
        #     return []
        if dict["state"] == state:
            output_list.append(dict)
        if "state" not in dict:
            raise KeyError("Неверное значение 'state'")
    return output_list

'EXECUTED'
# print(filter_by_state([{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], 'EXECUTED'))


def sort_by_date(list_dictionaries: list, reverse: bool = False) -> list:
    """
    Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате
    (date)

    # Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    """
    list_for_date = sorted(list_dictionaries, key=lambda x: x["date"], reverse=reverse)
    return list_for_date
