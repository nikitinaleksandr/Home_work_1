from mypy.state import state

from src.generators import filter_by_currency, transaction_descriptions
from src.utils import list_dict_transactions
from src.processing import sort_by_date
from pathlib import Path
current_dir = Path(__file__).parent.parent.resolve()
operations_file_json = current_dir/'data'/'operations.json'


def main_function():
    start_program = input("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          " 1. Получить информацию о транзакциях из JSON-файла\n"
          " 2. Получить информацию о транзакциях из CSV-файла\n"
          " 3. Получить информацию о транзакциях из XLSX-файла\n")
    list_transactions = []
    if int(start_program) == 1:
        print('Для обработки выбран JSON-файл')
        while True:
            choice_executed = input('Введите статус, по которому необходимо выполнить фильтрацию.'
                                    'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n').upper()
        # print(choice_executed)

            if choice_executed == 'EXECUTED':
                operations_file = list_dict_transactions(operations_file_json)
                for transaction in operations_file:
                    if 'state' in transaction:
                        list_transactions.append(transaction)
                        if transaction['state'] == 'EXECUTED':
                            print(transaction)
                break
            elif choice_executed == 'CANCELED':
                operations_file = list_dict_transactions(operations_file_json)
                for transaction in operations_file:
                    if 'state' in transaction:
                        if transaction['state'] == 'CANCELED':
                            print(transaction)
                break
            elif choice_executed == 'PENDING':
                operations_file = list_dict_transactions(operations_file_json)
                for transaction in operations_file:
                    if 'state' in transaction:
                        if transaction['state'] == 'PENDING':
                            print(transaction)
                break
            else:
                print(f'Статус операции {choice_executed} недоступен.')





                # EXECUTED_filter = list(filter(lambda x: x['state'] =='EXECUTED', i))
                # print(EXECUTED_filter)
    elif int(start_program) == 2:
        print('Для обработки выбран CSV-файл')
    elif int(start_program) == 3:
        print('Для обработки выбран XLSX-файл')


    print(list_transactions)

    filter_data = input('Отсортировать операции по дате? Да/Нет: ' ).lower()
    if filter_data == 'да':
        filter_direction = input('Отсортировать по возрастанию или по убыванию?: ').lower()
        if filter_direction == 'по возрастанию':
            # sorted_filter_data = sorted(list_transactions, key=lambda x:x['date'], reverse=False)
            sorted_filter_data= sort_by_date(list_transactions, False)
            print(sorted_filter_data)
        elif filter_direction == 'по убыванию':
            sorted_filter_data = sort_by_date(list_transactions, True)
            print(sorted_filter_data)
        filter_currency = input('Выводить только рублевые транзакции? Да/Нет: ').lower()
        if filter_currency == 'да':
            # return filter_by_currency(sorted_filter_data, "RUB")
            # print(sorted_filter_data)
            filtered_data = list(filter_by_currency(sorted_filter_data, currency="RUB"))
            print(filtered_data)
        elif filter_currency == 'нет':
            next()

        filter_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ').lower()
        if filter_word == 'да':
            filtered_descriptions = list(transaction_descriptions(filtered_data))
            print(filtered_descriptions)
            # print(sorted_filter_data)
        # sorted_filter_currency = sorted(filter_currency, key=lambda x:x['operationAmount']['currency']['RUB'])
        # print(sorted_filter_currency)
                # filter_word = input('Отфильтровать список транзакций по определенному слову в описании? '
                #                     'Да/Нет: ').lower()
                # if filter_word == 'да':
    # elif filter_data == 'нет':
    #     print(list_transactions)
    #     print(list_transactions
    #     if filter_direction == 'по возрастанию':
    #         filter_currency = input('Выводить только рублевые транзакции? Да/Нет: ' ).lower()
    #         if filter_currency == 'да':
    #             filter_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ' ).lower()
    #                 if filter_word == 'да':





    #     sorted_filter_data = sorted(list_transactions, key=lambda x:x['date'], reverse=False)
    #     print(sorted_filter_data)
    # elif filter_data == 'нет':
    #     sorted_filter_data = sorted(list_transactions, key=lambda x: x['date'], reverse=False)
    #     print(sorted_filter_data)
    #
    # filter_direction = input('Отсортировать по возрастанию или по убыванию?: ' ).lower()
    # if filter_direction == 'по возрастанию':
    #     pass
    # elif filter_direction == 'по убыванию':
    #     pass




if __name__ == '__main__':
     main_function()