import json
import os.path
from datetime import datetime


def get_json_data(json_file=f"..{os.sep}data{os.sep}operations.json"):
    """Чтение данных по операциям из json"""
    with open(json_file, encoding="utf-8") as fd:
        data = json.load(fd)
        return data


DT_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'


def get_last_operations(json_data):
    """
        Принимает список словарей, содержащих данные по выполненным операциям.
        Каждый словарь обязательно должен содержать поле 'date', иначе он не будет обработан.
        Возвращает список, который содержит последние op_count выполненных операций (status == 'EXECUTED'),
         отсортированный в порядке убывания значения поля 'date'
     """
    op_count = 5
    status = 'EXECUTED'
    date_field = 'date'
    state_field = 'state'

    operations = [operation for operation in json_data if date_field in operation]
    operations.sort(key=lambda operation: datetime.strptime((operation[date_field]), DT_FORMAT), reverse=True)
    with_status = list(filter(lambda operation: operation[state_field] == status, operations))

    return with_status[:op_count if op_count < len(with_status) else len(with_status)]


def mask(data):
    """
    Маскирует номер счета или номер карты в переданной строке.
    Номер счета заменяется на номер в формате  **XXXX (видны только последние 4 цифры номера счета).
    Номер карты заменяется на номер в формате  XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
    """
    data_list = data.split()
    number = data_list[-1]
    if 'Счет' in data:
        masked = '*' * (len(number) - 4) + number[-4:]
    else:
        masked = f'{number[0:4]} {number[4:6]}**  **** {number[-4:]}'
    return f"{' '.join(data_list[:len(data_list) - 1])} {masked}"


def print_operation(operation):
    """
    Вывод на экран данных по операции в формате:
        <дата перевода> <описание перевода>
        <откуда> -> <куда>
        <сумма перевода> <валюта>
    Дата  представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)
    """
    output_date_format = '%d.%m.%Y'
    print(f"{datetime.strptime(operation['date'], DT_FORMAT).strftime(output_date_format)} {operation['description']}")
    if 'from' in operation:
        print(f"{mask(operation['from'])} -> {mask(operation['to'])}")
    else:
        print(f"{mask(operation['to'])}")
    print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
