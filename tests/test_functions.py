import pytest

from src.functions import print_operation


@pytest.mark.parametrize('operation, expected', [
    (
            {
                "id": 207126257,
                "state": "EXECUTED",
                "date": "2019-07-15T11:47:40.496961",
                "operationAmount": {
                    "amount": "92688.46",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет 35737585785074382265"
            },
            "15.07.2019 Открытие вклада\nСчет 35737585785074382265\n92688.46 USD\n\n"
    ),
    (
            {
                "id": 957763565,
                "state": "EXECUTED",
                "date": "2019-01-05T00:52:30.108534",
                "operationAmount": {
                    "amount": "87941.37",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 46363668439560358409",
                "to": "Счет 18889008294666828266"
            },
            "05.01.2019 Перевод со счета на счет\nСчет 46363668439560358409 -> Счет 18889008294666828266\n"
            "87941.37 руб.\n\n"
    )])
def test_print_operation(capfd, operation, expected):
    print_operation(operation)
    out, _ = capfd.readouterr()
    assert out == expected
