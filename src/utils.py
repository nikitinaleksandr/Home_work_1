import json
from pathlib import Path
from typing import Union

current_dir = Path(__file__).parent.parent.resolve()
operations_file_json = current_dir/'data'/'operations.json'


def list_dict_transactions(operations_file_json: list) -> Union[list, dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    with open(operations_file_json, encoding='utf-8') as f:
        try:
            operations_file = json.load(f)
        except json.JSONDecodeError:
            print('Ошибка декодирования файла')
            return []
        return operations_file


print(list_dict_transactions(operations_file_json))


