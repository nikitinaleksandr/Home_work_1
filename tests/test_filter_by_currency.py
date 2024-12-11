import pytest

from src.generators import (card_number, card_number_generator,
                            filter_by_currency, transaction_descriptions)


def test_filter_by_currency(all_transactions) -> None:
    """
    Тестирование генератора описания операций с транзакциями
    - проверка, что функция корректно фильтрует транзакции в заданной валюте
    - проверка, что функция правильно отрабатывает случаи когда транзакция в заданной валюте отсутствует
    - проверка, что генератор не завершается ошибкой при обработке пустого списка или списка  без
    соответствующих валютных операций
    """

    usd_transactions = list(filter_by_currency(all_transactions, "USD"))
    assert usd_transactions == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                                 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                                 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                                 'to': 'Счет 11776614605963066702'},
                                {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                                 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                                 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                                 'to': 'Счет 75651667383060284188'}, {'id': 895315941, 'state': 'EXECUTED', 'date':
                                '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency':
                                {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from':
                                 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}]


def test_empty_currency():
    with pytest.raises(ValueError):
        next(filter_by_currency([{"id": 1, "state": "EXECUTED"}], ""))


@pytest.mark.parametrize("currency", ["GDR", "KZT"])
def test_wrong_currency(all_transactions, currency):
    with pytest.raises(ValueError):
        next(filter_by_currency(all_transactions, "currency"))


@pytest.mark.parametrize("transactions", [[]])
def test_empty_transaction(transactions):
    with pytest.raises(ValueError):
        next(filter_by_currency(transactions, "USD"))


@pytest.mark.parametrize("transactions", [[{"id": 1, "state": "EXECUTED"}]])
def test_wrong_transaction(transactions):
    with pytest.raises(ValueError):
        next(transaction_descriptions(transactions))


def test_transaction_descriptions(all_transactions) -> None:

    assert list(transaction_descriptions(all_transactions)) == ['Перевод организации', 'Перевод со счета на счет',
                                                                'Перевод со счета на счет', 'Перевод с карты на карту',
                                                                'Перевод организации']


@pytest.mark.parametrize("x, y, expected", [(1, 5, ['0000 0000 0000 0001', '0000 0000 0000 0002',
                                                    '0000 0000 0000 0003', '0000 0000 0000 0004',
                                                    '0000 0000 0000 0005'])])
def test_card_number_generator(x, y, expected) -> None:
    """Тестирование генератора card_number_generator. Правильность номеров карт в заданном диапазоне"""

    list_card_number_generator = list(card_number_generator(x, y))
    assert list_card_number_generator == expected


@pytest.mark.parametrize("x, y, expected", [(1, 5, ['0000 0000 0000 0001', '0000 0000 0000 0002',
                                                    '0000 0000 0000 0003', '0000 0000 0000 0004',
                                                    '0000 0000 0000 0005'])])
def test_correct_card_number_generator(x, y, expected):
    """Тестирование генератора card_number_generator. Корректность номеров карт"""
    assert (
            len(card_number) == 19
            and card_number[0:4].isdigit()
            and card_number[5:9].isdigit()
            and card_number[10:14].isdigit()
            and card_number[15:19].isdigit()
            and card_number[4] == " "
            and card_number[9] == " "
            and card_number[14] == " "
            )


@pytest.mark.parametrize("x, y", [(-1, 9999999999), (5, 100000000000000000000000)])
def test_range_card_number_generator(x, y):

    with pytest.raises(ValueError):
        next(card_number_generator(x, y))
