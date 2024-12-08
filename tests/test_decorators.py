import pytest
from src.decorators import log


#
def test_log():
    """Тестирование правильности работы декоратора"""
    @log(filename = "mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(2, 3)
    assert result == 5
# @log()
# def my_function(x, y):
#     return x + y


# def test_error_in_log(capsys):
#     my_function()
#     captured = capsys.readouterr()
#     assert captured.out == "Function my_function called whith args: (2, 3) and kwargs: {}. Result: 5" in captured.out

