import json
from datetime import datetime
from pprint import pprint


def load_data(file_path='operations.json'):
    """
    выгружает json файл
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def get_last(operations):
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


def masked_number(operation):
    """
    маскирует номер
    """
    number = operation.split()[-1]
    if len(number) == 16:
        musk_numb = number[:4] + " " + number[4:6] + "** ****" + number[-4:]
        return ' '.join(operation.split()[:-1]) + ' ' + musk_numb
    else:
        musk_numb = "**" + number[-4:]
        return ' '.join(operation.split()[:-1]) + ' ' + musk_numb




def change_date(self):
    """
    метод изменяет дату в нужном формате
    """
    date_from_str = datetime.strptime(self, '%Y-%m-%dT%H:%M:%S.%f')
    return date_from_str.strftime('%d.%m.%Y')




