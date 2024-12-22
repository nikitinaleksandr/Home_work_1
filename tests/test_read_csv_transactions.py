from unittest.mock import patch, mock_open
from src.cvs_xlsx import read_csv_transactions


@patch('src.cvs_xlsx.open', new_callable=mock_open,
       read_data='id,state,date\n441945886,EXECUTED,2019-08-26T10:50:58.294041\n')
def test_read_csv_transactions(mock_file):
    result = read_csv_transactions('dir_transactions')
    assert result == [{'id': '441945886', 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'}]
