def get_mask_account(number_account: str) -> str:
    """
        Функция, которая принимает на вход счета и возвращает ее маску.
    """
    str_number_account = str(number_account)
    return f"**{str_number_account[-4:]}"


#print(get_mask_account(1234567891234567))


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
    return (
        f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"
    )


#print(get_mask_card_number(1234567898765432))
