import logging
from pathlib import Path
# from venv import logger

current_dir = Path(__file__).parent.parent.resolve()
log_utils_file = current_dir/'logs'/'masks.log'


logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_utils_file, mode='w',  encoding="utf-8")
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_account(number_account: str) -> str:
    """
    Функция, которая принимает на вход номер счета и возвращает его маску.
    """
    str_number_account = str(number_account)
    if len(str_number_account[-16::]) != 16:
        logger.error("Некорректная длина номера счета")
        raise ValueError("Некорректная длина номера счета")

    else:
        logger.info('Вывод номера счета')
        return f"**{str_number_account[-4:]}"


print(get_mask_account(1234567891234567))


def get_mask_card_number(number_card: str) -> str:
    """

    Функция, которая принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX

    Пример ввода:
    7000792289606361

    Пример вывода:
    7000 79** **** 6361
    """

    str_number_card = str(number_card)
    if number_card == "":
        logger.error("Строка должна содержать номер карты")
        raise ValueError("Строка должна содержать номер карты")
    logger.info('Вывод номера карты')
    return f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"


print(get_mask_card_number(1234567898765432))
