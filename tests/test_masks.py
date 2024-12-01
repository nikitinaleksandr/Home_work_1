import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account() -> None:
    """Тестирование правильности маскировки счета"""
    assert get_mask_account("1234567891234567") == "**4567"


@pytest.mark.parametrize("number_account", ["1234567891234567", "9876543210987654"])
def test_masks_len_account_number(number_account: str) -> None:
    """Тестирование нестандартных длин номеров счетов"""
    assert len(number_account) == 16


@pytest.mark.parametrize("number_account", ["1234567891234567", "9876543210987654"])
def test_masks_wrong_type(number_account: str) -> None:
    """Тестирование нестандартных типов номеров счетов"""
    assert number_account.isdigit()


def test_masks_len_account_short() -> None:
    """Тестирование ввода короткого номера счета"""
    with pytest.raises(ValueError):
        get_mask_account("12345678912345")


def test_get_mask_card_number() -> None:
    """Тестирование правильности маскировки карты"""
    assert get_mask_card_number("1234567898765432") == "1234 56** **** 5432"


@pytest.mark.parametrize("number_card", ["1234567891234567", "9876543210987654"])
def test_get_mask_card_number_len_card_number(number_card: str) -> None:
    """Тестирование нестандартных длин номеров карт"""
    assert len(number_card) == 16


@pytest.mark.parametrize("number_card", ["1234567891234567", "9876543210987654"])
def test_get_mask_card_number_wrong_type(number_card: str) -> None:
    """Тестирование неправильных типов номеров карт"""
    assert number_card.isdigit()


def test_no_number_card() -> None:
    """Тестирование отсутствия ввода номеров карт"""
    with pytest.raises(ValueError):
        get_mask_card_number("")
