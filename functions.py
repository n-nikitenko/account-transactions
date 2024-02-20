import json
import os.path


def get_json_data():
    """Чтение данных по операциям из json"""
    with open(os.path.join("data", "operations.json"), encoding="utf-8") as json_file:
        data = json.load(json_file)
        return data

