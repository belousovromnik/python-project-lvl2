import json
from gendiff.constants import DEBUG


def generate_diff(file_before, file_after):
    f_before = json.load(open(file_before))
    f_after = json.load(open(file_after))

    # берем ключи первого файла, добавляем к ним ключи второго файла, 
    # создаем множество
    union_uniq_keys = set(f_before.keys()).union(set(f_after.keys()))

    result = '{'
    for key in union_uniq_keys:
        # считываем значения из первого и второго массивов, 
        # если значения нет - будет None
        file1_value = f_before.get(key)
        file2_value = f_after.get(key)

        if DEBUG:
            print('{} - {} - {}'.format(key, file1_value, file2_value))

        if file1_value == file2_value:
            result += string_format(key, file1_value, ' ')
        else:
            if file1_value:
                result += string_format(key, file1_value, '-')
            if file2_value:
                result += string_format(key, file2_value, '+')

    result += '\n}'
    return result


def string_format(key, value, operator):
    return '\n  {} {}: {}'.format(operator, key, value)
