from src.decorators import log


def test_log():
    """Тестирование правильности работы декоратора"""
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(2, 3)
    assert result == 5


@log()
def my_function(x, y):
    return x + y


def test_empty_filename_in_log(capsys):
    """Тестирование на работу функции в случае ввода неверных данных"""
    my_function('2', 3)
    captured = capsys.readouterr()
    assert 'my_function' in captured.out
