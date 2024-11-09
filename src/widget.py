from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_by_card: str) -> str:
    """
    Функция mask_account_card принимает на вход строку формата
    Visa Platinum 7000792289606361, или Maestro 7000792289606361,
    или Счет 73654108430135874305. Для маскировки номера карты/счета
    используются ранее написанные функции из модуля masks

    Пример для карты
    Visa Platinum 7000792289606361 - входной аргумент
    Visa Platinum 7000 79** **** 6361 - выход функции

    Пример для счета
    Счет 73654108430135874305 - входной аргумент
    Счет **4305 - выход функции
    """
    str_info_by_card = str(info_by_card)
    if "Счет" in info_by_card:
        return f"Счет {get_mask_account(str_info_by_card)}"
    else:
        return f"{str_info_by_card[0:-17]}: {get_mask_card_number(str_info_by_card[-16::])}"


print(mask_account_card("Счет 5647839058876378"))


def get_date(card_data: str) -> str:
    """
    Функция, которая принимает на вход строку, с датой в
    формате "2024-03-11Т02:26:18.671407" и возвращает строку
    с датой в формате "ДД.ММ.ГГГГ" (11.03.2024)
    """
    # str_get_date = str(card_data)
    return f"{card_data[8:10]}.{card_data[5:7]}.{card_data[0:4]}"


print(get_date("2024-03-11Т02:26:18.671407"))
