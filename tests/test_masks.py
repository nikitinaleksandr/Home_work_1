import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account('1234567891234567') == '**4567'


@pytest.mark.parametrize ("number_account", ["1234567891234567", "9876543210987654"])

def test_masks_len_account_number(number_account):
    assert len(number_account) == 16

@pytest.mark.parametrize ("number_account", ["1234567891234567", "9876543210987654"])
def test_masks_wrong_type(number_account):
    assert number_account.isdigit() == True


def test_masks_len_account_short():
    with pytest.raises(ValueError):
        get_mask_account('12345678912345')


def test_get_mask_card_number():
    assert get_mask_card_number('1234567898765432') == '1234 56** **** 5432'


@pytest.mark.parametrize ("number_card", ["1234567891234567", "9876543210987654"])
def test_get_mask_card_number_len_card_number(number_card):
    assert len(number_card) == 16

@pytest.mark.parametrize ("number_card", ["1234567891234567", "9876543210987654"])
def test_get_mask_card_number_wrong_type(number_card):
    assert number_card.isdigit() == True


def test_no_number_card():
    with pytest.raises(TypeError):
        get_mask_card_number()




