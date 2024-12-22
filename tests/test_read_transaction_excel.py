from unittest.mock import patch

import pandas as pd

from src.cvs_xlsx import read_transactions_excel


@patch('src.cvs_xlsx.pd.read_excel')
def test_read_transactions_excel(mock_transactions_excel):
    mock_transactions_excel.return_value = pd.DataFrame([{'id': 441945886, 'state': 'EXECUTED', 'date':
                                                          '2019-08-26T10:50:58.294041'}])
    assert read_transactions_excel('dir_transactions') == [{'id': 441945886, 'state': 'EXECUTED', 'date':
                                                            '2019-08-26T10:50:58.294041'}]
