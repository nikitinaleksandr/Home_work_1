import pytest
from src.widget import mask_account_card, get_date


# Функция mask_account_card
def test_mask_account_card() -> None:
    """Тестирование правильности маскировки счета и карты"""
    assert mask_account_card("Счет 5647839058876378") == "Счет **6378"
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum: 7000 79** **** 6361"


@pytest.mark.parametrize("info_by_card", ["Счет F 1234567891234567", "Maestro 9876543210987654"])
def test_widget_len_account_and_len_number_card(info_by_card: str) -> None:
    """Проверка работы функции с различными форматами и длинами номеров счетов"""
    assert (
        len(info_by_card[-16::]) == 16
        and info_by_card[-16::].isdigit()
        and not info_by_card[-17::].isdigit()
    )


def test_no_info_by_card() -> None:
    """Проверка работы функции при отсутствии ввода данных"""
    with pytest.raises(TypeError):
        mask_account_card()


# Функция get_data
def test_get_date() -> None:
    """Тестирование проверки правильности преобразования даты"""
    assert get_date("2024-03-11Т02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("card_data", ["2024-03-11Т02:26:18.671407", "2024-12-11Т02:26:18.671408"])
def test_get_date_by_different_parameter(card_data: str) -> None:
    """Тестирование нестандартных длин и форматов дат"""
    assert (
        len(card_data) == 26
        and card_data[0:4].isdigit()
        and card_data[5:7].isdigit()
        and card_data[8:10].isdigit()
        and card_data[4] == "-"
        and card_data[7] == "-"
        and card_data[10] == "Т"
        and 0 < int(card_data[8:10]) <= 31
        and 0 < int(card_data[5:7]) <= 12
        and int(card_data[0:4]) == 2024
    )


def test_no_get_date() -> None:
    """Тестирование на корректность работы при отсутствии даты"""
    with pytest.raises(TypeError):
        get_date()
