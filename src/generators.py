from typing import Union
# from wsgiref.validate import assert_


def filter_by_currency(transactions: Union[list, dict], currency: str) -> Union[list, dict]:
    """
    Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта
    операции соответствует заданной (например, USD).
    """
    if currency == "":
        raise ValueError("Не указана валюта транзакции")
    if currency not in ["USD", "RUB", "EURO"]:
        raise ValueError("Неверная валюта")
    if transactions == []:
        raise ValueError("Отсутствует список транзакций")
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def transaction_descriptions(transactions: Union[list, dict]) -> str:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    if transactions == []:
        raise ValueError("Отсутствует список транзакций")
    for item in transactions:
        if not item.get("description"):
            raise ValueError("Отсутствует описание транзакций")
        yield item["description"]


def card_number_generator(start: str, stop: str) -> str:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.

    Пример использования функции:
    for card_number in card_number_generator(1, 5):
        print(card_number)

    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
    """

    for num in range(start, stop + 1):
        card_number = str(num)
        while len(card_number) < 16:
            card_number = '0' + card_number

        # if 1 > int(card_number) or int(card_number) > 9999999999999999:
        if 1 > start>9999999999999999 or stop > 9999999999999999:
            raise ValueError("недопустимый номер карты")

        form_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        if 1 <= int(card_number) <= 9999999999999999:
            yield form_card_number


transactions = (
    [
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
)


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(3):
    print(next(usd_transactions))

# RUB_transactions = filter_by_currency(transactions, "RUB")
# for _ in range(2):
#     print(next(RUB_transactions))

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

for card_number in card_number_generator(1, 5):
    print(card_number)
