import os
from dbm import error
from fileinput import filename
from pathlib import Path
from functools import wraps
from mypy.util import os_path_join

current_dir = Path(__file__).parent.parent.resolve()
log_scripts = current_dir/'data'/'mylog.txt'

def log(filename=None):
    def logging(func):
        def wrapper(*args, **kwargs):

            print('До выполнения функции')

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error_message = str(e).__name__
            if filename is None:

                print(f'Function {func.__name__}: {error_message}. Inputs: {args}, kwargs: {kwargs}.')
                # raise TypeError(f'Function {func.__name__} Inputs: {args}, kwargs: {kwargs}.')
            if filename == "":
                print('Not filename')
            else:
                with open(log_scripts, "a") as file:
                    file.write(f'Function {func.__name__} called whith args: {args} and kwargs: {kwargs}. Result: {result}\n')

            print('После выполнения функции')
            return result
        return wrapper
    return logging

@log('2')
def my_function(x, y):
    return x + y
my_function(2, 3)






    #      def inner(*args, **kwargs):
    #         result = func(*args, **kwargs)
    #
    #         if result == filename():
    #             result = func()
    #         pass# как записать лог в указанный файл?
    #     else:
    #         print('вывод логов в консоль')
    #
    #
    # return wrapper







    # return x + y
