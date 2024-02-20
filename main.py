from functions import get_last_five_operations, get_json_data, print_operation

for op in get_last_five_operations(get_json_data()):
    print_operation(op)
