from locale import currency
from typing import Union
import json
from pathlib import Path
from json import JSONDecodeError
import requests
from blib2to3.pytree import convert

current_dir = Path(__file__).parent.parent.resolve()
operations_file_json = current_dir/'data'/'operations.json'
from dotenv import load_dotenv
import os

load_dotenv('../.env')

def sum_transactions(operations_file: dict[str, float]) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса
    валют и конвертации суммы операции в рубли.
    """

    if operations_file ["operationAmount"]["currency"]["code"] == "RUB":
        return operations_file["operationAmount"]["amount"]
    else:
        API_KEY = os.getenv('API_KEY')
        convert_to = "RUB"
        convert_from = operations_file["operationAmount"]["currency"]["code"]
        amount = operations_file["operationAmount"]["amount"]

        url = f"https://api.apilayer.com/currency_data/convert?to={convert_to}&from={convert_from}&amount={amount}"


        payload = {}
        headers= {
          "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        result = response.json()
        return result['result']

print(
sum_transactions(
{
"id": 41428829,
"state": "EXECUTED",
"date": "2019-07-03T18:35:29.512364",
"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
"description": "Перевод организации",
"from": "MasterCard 7158300734726758",
"to": "Счет 35383033474447895560",
}
)
)