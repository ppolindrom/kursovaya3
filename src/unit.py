import json


def load_data():
    """
    выгружает json файл
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def get_last_op(operations):
    """
    выбирает из словаря 5 операций executed
    """
    last_operation = []
    for i in operations[::-1]:
        if i['state'] == 'EXECUTED':
            last_operation.append(i)
            if len(last_operation) == 5:
                break
    return last_operation

def sorted_operation(operations):
    """
    сортирует по дате
    """
    for i in range(len(operations) - 1):
        for j in range(len(operations) - i - 1):
            if operations[j]['date'] < operations[j + 1]['date']:
                operations[j], operations[j + 1] = operations[j + 1], operations[j]
    return operations

