from pathlib import Path

from src.cvs_xlsx import read_csv_transactions, read_transactions_excel
from src.generators import filter_by_currency
from src.masks import get_mask_account
from src.processing import sort_by_date
from src.seach_with_re import search_with_str
from src.utils import list_dict_transactions
from src.widget import get_date

current_dir = Path(__file__).parent.parent.resolve()
operations_file_json = current_dir/'data'/'operations.json'
dir_transactions_excel = current_dir/'transactions_excel.xlsx'
dir_transactions = current_dir/'transactions.csv'


def main_function():
    '''Функция, которая связывает функциональности проекта между собой'''
    start_program = input("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n Выберите "
                          "необходимый пункт меню:\n 1. Получить информацию о транзакциях из JSON-файла\n 2. Получить "
                          "информацию о транзакциях из CSV-файла\n 3. Получить информацию о транзакциях из "
                          "XLSX-файла\n")
    list_transactions = []

    if int(start_program) == 1:
        operations_file = list_dict_transactions(operations_file_json)
        print('Для обработки выбран JSON-файл')

    elif int(start_program) == 2:
        operations_file = read_csv_transactions(dir_transactions)
        print('Для обработки выбран CSV-файл')

    elif int(start_program) == 3:
        operations_file = list(read_transactions_excel(dir_transactions_excel))
        print('Для обработки выбран XLSX-файл')

    while True:
        choice_executed = input('Введите статус, по которому необходимо выполнить фильтрацию.'
                                'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n').upper()
    # print(choice_executed)
        if choice_executed == 'EXECUTED':
            for transaction in operations_file:
                if 'state' in transaction:
                    if transaction['state'] == 'EXECUTED':
                        list_transactions.append(transaction)

                        print(transaction)
            break
        elif choice_executed == 'CANCELED':
            operations_file = list_dict_transactions(operations_file_json)
            for transaction in operations_file:
                if 'state' in transaction:
                    if transaction['state'] == 'CANCELED':
                        list_transactions.append(transaction)
                    # if transaction['state'] == 'CANCELED':
                        print(transaction)
            break
        elif choice_executed == 'PENDING':
            operations_file = list_dict_transactions(operations_file_json)
            for transaction in operations_file:
                if 'state' in transaction:
                    if transaction['state'] == 'PENDING':
                        list_transactions.append(transaction)

                    # if transaction['state'] == 'PENDING':
                    #     return transaction
            break
        else:
            print(f'Статус операции {choice_executed} недоступен.')

    if not list_transactions:
        print('Не найдено ни одной транзакции, подходящей под ваши условия')
        return

    filter_data = input('Отсортировать операции по дате? Да/Нет: ').lower()
    if filter_data == 'да':
        filter_direction = input('Отсортировать по возрастанию или по убыванию?: ').lower()
        if filter_direction == 'по возрастанию':
            sorted_filter_data = sort_by_date(list_transactions, False)
            print(sorted_filter_data)
        elif filter_direction == 'по убыванию':
            sorted_filter_data = sort_by_date(list_transactions, True)
            print(sorted_filter_data)
    elif filter_data == 'нет':
        sorted_filter_data = list_transactions
        print(sorted_filter_data)

    filter_currency = input('Выводить только рублевые транзакции? Да/Нет: ').lower()
    if filter_currency == 'да':
        filtered_currency = list(filter_by_currency(sorted_filter_data, currency="RUB"))
        print(filtered_currency)
    elif filter_currency == 'нет':
        filtered_currency = sorted_filter_data
        print(filtered_currency)

    filter_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ').lower()
    if filter_word == 'да':
        filtered_descriptions = search_with_str(filtered_currency, 'Перевод организации')
        print(filtered_descriptions)
    elif filter_word == 'нет':
        filtered_descriptions = filtered_currency
        print(filtered_descriptions)
    # counted = Counter(filtered_descriptions)
    items = 0
    for item in filtered_descriptions:
        items += 1
    # counted = Counter(item['state'] for item in filtered_descriptions)
    # print(counted)

    print('Распечатываю готовый список транзакций...')
    print(f'Всего банковских транзакций в выборке: {items}')
    if filtered_descriptions == []:
        print('Не найдено ни одной транзакции, подходящей под ваши условия')
    else:
        for item in filtered_descriptions:
            print(f"\n{get_date(item['date'])} {item['description']}\n {get_mask_account(item['to'])}\n "
                  f"Сумма: {item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")


if __name__ == '__main__':
    main_function()
