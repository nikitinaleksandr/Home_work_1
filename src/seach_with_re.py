import re
from itertools import count
from typing import Union
# from src.generators import transactions
from mypy.util import get_class_descriptors
from collections import Counter
transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


# def search_with_str(transactions: Union[list, dict], pattern: str) -> dict[str]:
#     """
#     Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
#     а возвращать список словарей, у которых в описании есть данная строка
#     """

#     list_transaction = []
#     for trans in transactions:
#         # print(trans)
#
#         pattern = r'Перевод организации'
#         get_transactions = re.findall(pattern, str(trans['description']))
#         if get_transactions != []:
#             list_transaction.append(trans)
#     return list_transaction
#
# if __name__ == '__main__':
#     result = search_with_str(transactions, 'Перевод организации')
#     print(result)


def search_description_with_str(transactions: Union[list, dict], dict_description: dict) -> dict[str]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории.
    """
    dict_transaction = {}
    list_description = []
    for trans in transactions:
        list_description.append(trans['description'])
    # print(list_description)
    counted = Counter(list_description)
    return dict(counted)


if __name__ == '__main__':
     result = search_description_with_str(transactions,  ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"])
     print(result)







# Категории операций хранятся в поле
# description
# .
#
# Расположение новой функции в структуре проекта определите самостоятельно.