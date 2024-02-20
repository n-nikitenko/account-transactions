import json
import os.path
from datetime import datetime
from pprint import pprint


def get_json_data():
    """Чтение данных по операциям из json"""
    with open(os.path.join("data", "operations.json"), encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


def get_last_five_operations(json_data):
    """
        Принимает список словарей, содержащих данные по выполненным операциям.
        Каждый словарь обязательно должен содержать поле 'date', иначе он не будет обработан.
        Возвращает список, который содержит последние пять выполненных операций, отсортированный
        в порядке убывания значения поля 'date'
     """
    op_count = 5
    status = 'EXECUTED'
    date_field = 'date'
    state_field = 'state'
    dt_format = '%Y-%m-%dT%H:%M:%S.%f'

    operations = [operation for operation in json_data if date_field in operation]
    operations.sort(key=lambda operation: datetime.strptime((operation[date_field]), dt_format), reverse=True)
    with_status = list(filter(lambda operation: operation[state_field] == status, operations))

    return with_status[:op_count if op_count < len(with_status) else len(with_status)]

