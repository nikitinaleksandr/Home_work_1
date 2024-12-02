import pytest

from src.processing import filter_by_state, sort_by_date

# Функция filter_by_state

# @pytest.mark.parametrize('list_dictionaries, state',
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], 'CANCELED')


def test_filter_by_state() -> None:
    """Тестирование фильтрации по статусу 'state'"""
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        "CANCELED",
    ) == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_filter_no_state() -> None:
    """Тестирование при отсутствии в словаре статуса 'state'"""
    with pytest.raises(KeyError):
        filter_by_state(
            [
                {"id": 41428829, "tate": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "tate": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "tate": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "tate": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            "CANCELED",
        )


def test_filter_for_any_state() -> None:
    """Тестирование различных значений статуса 'state'"""
    with pytest.raises(ValueError):
        filter_by_state(
            [
                {"id": 41428829, "state": "XECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "ANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "ANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "XECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            "ANCELED",
        )


# Функция sort_by_date


def test_sort_by_date_decreasing() -> None:
    """Тестирование сортировки словарей по статусу 'date' убывание"""
    assert sort_by_date(
        [
            {"id": 41428829, "state": "XECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "ANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "ANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 939719570, "state": "XECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        True,
    ) == [
        {"id": 41428829, "state": "XECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "ANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "ANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "XECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_up() -> None:
    """Тестирование сортировки словарей по статусу ''date' возрастание"""
    assert sort_by_date(
        [
            {"id": 41428829, "state": "XECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "ANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "ANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 939719570, "state": "XECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        False,
    ) == [
        {"id": 939719570, "state": "XECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "ANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "ANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "XECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_ident() -> None:
    """Проверка корректности сортировки при одинаковых датах"""
    assert sort_by_date(
        [
            {"id": 41428829, "state": "XECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "ANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "ANCELED", "date": "2018-09-12T08:21:33.419441"},
            {"id": 939719570, "state": "XECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        False,
    ) == [
        {"id": 939719570, "state": "XECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "ANCELED", "date": "2018-09-12T08:21:33.419441"},
        {"id": 594226727, "state": "ANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "XECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize("data", ["2024-03-11Т02:26:18.671407", "2024-12-11Т02:26:18.671408"])
def test_get_date_by_different_param(data: str) -> None:
    """Тестирование на работу функции с нестандартными и некорректными формами дат"""
    assert (
        len(data) == 26
        and data[0:4].isdigit()
        and data[5:7].isdigit()
        and data[8:10].isdigit()
        and data[4] == "-"
        and data[7] == "-"
        and data[10] == "Т"
        and 0 < int(data[8:10]) <= 31
        and 0 < int(data[5:7]) <= 12
        and 2000 < int(data[0:4]) <= 2024
    )
