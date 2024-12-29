#**Виджет банковских операций клиента**
Это виджет, который показывает несколько последних успешных операций клиента.
Статус проекта: *в разработке.*
Проект протестирован на 98 %.

## Описание
Проект содержит следующие функции:
- функцию маскировки номера банковской карты или банковского счета
- функцию фильтрации завершенных и не завершенных операций клиента
- функцию сортировки операций клиента по дате их выполнения
- функция, которая поочередно выдает транзакции с определенной валютой (например, USD)
- функция описания выполненных транзакций
- функция генерации номеров карт
- декоратор, который логирует начало и конец выполнения функции, а также ее результаты и возникшие ошибки
- функция для считывания финансовых операций в Excel
- функция для считывания финансовых операций в CSV файла
- функция, которая принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список 
  словарей, у которых в описании есть данная строка
- функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
  а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций
  в каждой категории
- функция связываюзая все функциональности проекта 
### Установка и использование
С помощью git clone клонируем репозиторий на свой компьютер

#### Примеры использования
1. Маскировка номера карты и номера счета

Пример для карты:
    Visa Platinum 7000792289606361 - входной аргумент
    Visa Platinum 7000 79** **** 6361 - выход функции

Пример для счета:
    Счет 73654108430135874305 - входной аргумент
    Счет **4305 - выход функции

2. Фильтрация завершенных и незавершенных операций клиента
    
Входные данные:
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

Выходные данные:

Выход функции со статусом по умолчанию 'EXECUTED'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

Выход функции, если вторым аргументов передано 'CANCELED'
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

3. Сортировка операций клиента по дате их выполнения

Входные данные:
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

Выходные данные:
   [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

4. Транзакции с заданной валютой

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
         
     "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }


###Тестирование

Проведено тестирование функций:

Модуль masks
1. Функция get_mask_account:
- Тестирование правильности маскировки счета.
- Тестирование нестандартных длин номеров счетов.
- Тестирование нестандартных типов номеров счетов.
- Тестирование ввода короткого номера счета.

2. Функция get_mask_card_number:
- Тестирование правильности маскировки карты.
- Тестирование нестандартных длин номеров карт.
- Тестирование неправильных типов номеров карт.
- Тестирование отсутствия ввода номеров карт.

Модуль widget
3. Функция mask_account_card:
- Тестирование правильности маскировки счета и карты.
- Проверка работы функции с различными форматами и длинами 
номеров счетов.
- Проверка работы функции при отсутствии ввода данных.

4. Функция get_date:
- Тестирование проверки правильности преобразования даты.
- Тестирование нестандартных длин и форматов дат.
- Тестирование на корректность работы при отсутствии дат.

Модуль processing
5. Функция filter_by_state:
- Тестирование фильтрации по статусу 'state'.
- Тестирование при отсутствии в словаре статуса 'state'.
- Тестирование различных значений статуса 'state'.

6. Функция sort_by_date:
- Тестирование сортировки словарей по статусу 'date' убывание.
- Тестирование сортировки словарей по статусу 'date' возрастание.
- Проверка корректности сортировки при одинаковых датах.
- Тестирование на работу функции с нестандартными и некорректными 
формами дат.

Модуль filter_by_currency
7. Функция filter_by_currency
- Тестирование корректной фильтрации транзакции в заданной валюте
- Тестирование функции на правильность работы в случае, когда транзакция в заданной валюте отсутствует
- Тестирование, что генератор не завершается ошибкой при обработке пустого списка или списка без
  соответствующих валютных операций

8. Функция transaction_descriptions
- Тестирование корректного описания для каждой транзакции
- Тестирование работы функции при пустом списке транзакций

9. Функция card_number_generator
- Тестирование правильности номеров карт в заданном диапазоне
- Тестирование корректности формирования номеров карт
- Тестирование корректности обработки крайних результатов диапазона генерации

Модуль decorators
10. Декоратор log
- Тестирование правильности работы декоратора при наличии входных данных
- Тестирование правильности работы декоратора при неверных входных данных

Moдуль csv_xlcx

11. Функция read_csv_transactions
- Тестирование правильности чтения файла CSV

12. Функция read_transactions_excel
- Тестирование правильности чтения файла Excel

