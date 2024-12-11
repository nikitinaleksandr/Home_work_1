from pathlib import Path

current_dir = Path(__file__).parent.parent.resolve()
log_scripts = current_dir/'data'/'mylog.txt'


def log(filename="mylog.txt"):
    """Декоратор, который логирует начало и конец выполнения функции, а также ее результаты и возникшие ошибки"""
    def logging(func):
        def wrapper(*args, **kwargs):

            print('До выполнения функции')
            # error_message = None


            try:
                result = func(*args, **kwargs)
                raise func(*args, **kwargs)

            except Exception as e:

                error_message = str(e)
                print(f'Function {func.__name__}: {error_message}. Inputs: {args}, kwargs: {kwargs}.')
            if filename == "":
                print('Not filename')
            else:
                with open(log_scripts, "a") as file:
                    file.write(f'{func.__name__} ok\n')

            print('После выполнения функции')
            return result
        return wrapper
    return logging


@log()
def my_function(x, y):
    """Функция сложения двух чисел"""

    # if type(x) != int or type(y) != int:
    #     raise TypeError("Неверный тип данных")
    return x + y


my_function('2', 3)
