import os
from unittest.mock import patch

import requests
from unittest import mock

from src.utils import list_dict_transactions


@patch("json.load")
def test_list_dict_transactions(mock_get):
    mock_get.return_value = []
    assert list_dict_transactions("C:\\Users\\Nikit\\my_prj\\Home_work_1\\data\\operations.json") == []



