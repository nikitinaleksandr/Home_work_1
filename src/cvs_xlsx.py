import csv
from pathlib import Path
import pandas as pd

current_dir = Path(__file__).parent.parent.resolve()
dir_transactions = current_dir/'transactions.csv'
dir_transactions_excel = current_dir/'transactions_excel.xlsx'


def read_csv_transactions(dir_transactions: str) -> list:
    """
    Функция для считывания финансовых транзакций из CSV,
    принимает путь к файлу в качестве аргумента
    результат выводится в виде списка словарей.
    """
    list_dict = []
    with (open(dir_transactions, "r", encoding="utf-8") as file):
        reader = csv.DictReader(file)
        for row in reader:
            list_dict.append(row)
            return list_dict
            print(list_dict)


read_csv_transactions(dir_transactions)


def read_transactions_excel(dir_transactions: str) -> list:
    """
    Функция для считывания финансовых транзакций из Excel,
    принимает путь к файлу Excel в качестве аргумента.
    Результат выводится в виде списка словарей.
    """
    excel_data = pd.read_excel(dir_transactions_excel)
    # print(excel_data)
    excel_data_dict = excel_data.to_dict(orient='records')
    return excel_data_dict


read_transactions_excel(dir_transactions_excel)


# df_csv = pd.read_csv("D:/transactions.csv")
# print(df_csv.shape)
# print(read_csv_transactions('transactions.csv'))
#     df_csv = pd.read_csv("D:/transactions.csv")
#
#     return df_csv
#
# if __name__ == '__main__':
#     print transactions = read_csv('transactions.csv')
# df_csv = pd.read_csv("D:/transactions.csv")
# print(df_csv)


# def read_csv_transactions(transactions: str) -> list:
#     df = pd.read_csv('dir_transactions.csv')


# if __name__ == '__main__':
#     read_csv_transactions(df_csv)

# df = pd.read_excel("D:/transactions_excel.xlsx")
# print(df.shape)
# print(df.head())
