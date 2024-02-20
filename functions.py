import json
import os.path
from datetime import datetime


def get_json_data():
    """Чтение данных по операциям из json"""
    with open(os.path.join("data", "operations.json"), encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data


def get_last_five_operations(json_data):
    """
        Принимает список словарей, содержащих данные по операциям.
        Каждый словарь обязательно должен содержать поле 'date', иначе он не будет обработан.
        возвращает список, который содержит последние пять операций, отсортированный
        в порядке убывания значения поля 'date'
     """
    operations = [operation for operation in json_data if 'date' in operation]
    operations.sort(key=lambda operation: datetime.strptime((operation['date']), "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return operations[:5]
