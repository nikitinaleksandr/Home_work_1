from shlex import quote
from unittest.mock import patch

from src.external_api import sum_transactions


@patch('requests.request')
def test_sum_transactions_RUB(mock_get):
    ""
    mock_get.return_value = {"operationAmount":{"amount": 1, "currency": {"code": "RUB"}}}
    assert sum_transactions({"operationAmount":{"amount": 1, "currency": {"code": "RUB"}}}) == 1

# @patch('requests.request')
# def test_sum_transactions_USD(mock_get):
#     mock_get.return_value.text = '{'result': 1}'
#     assert sum_transactions({"operationAmount":{"amount": 1, "currency": {"code": "USD"}}}) == 1


@patch('requests.request')
def test_sum_transactions_USD(mock_get):
    mock_get.return_value.text='{"result": 1}'
    assert sum_transactions({"operationAmount":{"amount": 1, "currency": {"code": "USD"}}}) == 1





