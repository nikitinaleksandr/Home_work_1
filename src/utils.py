from locale import currency
from typing import Union
import json
from pathlib import Path
from json import JSONDecodeError
import requests
current_dir = Path(__file__).parent.parent.resolve()
operations_file_json = current_dir/'data'/'operations.json'


def list_dict_transactions(operations_file_json: list) -> Union[list, dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    with open (operations_file_json, encoding='utf-8') as f:
        try:
            operations_file = json.load(f)
        except json.JSONDecodeError:
            print('Ошибка декодирования файла')
            return []
        return operations_file

print(list_dict_transactions(operations_file_json))


# def sum_transactions(transaction: dict[str, float]) -> float:
#     """
#     Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
#     float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса
#     валют и конвертации суммы операции в рубли.
#     """
#     try:
#         with open (operations_file_json, encoding='utf-8') as f:
#             try:
#                 operations_file = json.load(f)
#             except json.JSONDecodeError:
#                 print('Ошибка декодирования файла')
#                 return False
#     except FileNotFoundError:
#         print("Файл не найден")
#         return False
#
#     amount_sum = 0
#     for amount in operations_file:
#         amount_sum += float(amount["operationAmount"]["amount"])
#         return amount_sum
#
#     # sum_trans = sum(operations_file["operationAmount"]["amount"].values())
#     # print(sum_trans)
#
# print(sum_transactions(operations_file_json))
