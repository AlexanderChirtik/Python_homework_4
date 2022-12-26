# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

import random


def new_file(text):
    with open('file.txt', 'w') as data:
        data.write(text)


def ran():
    return random.randint(0, 101)


def subsequence(x):
    elements = [ran() for i in range(x+1)]
    return elements


def new_text(list_in):
    double_list = list_in[::-1]
    record = ''
    if len(double_list) < 1:
        record = 'x = 0'
    else:
        for i in range(len(double_list)):
            if i != len(double_list) - 1 and double_list[i] != 0 and i != len(double_list) - 2:
                record += f'{double_list[i]}x^{len(double_list)-i-1}'
                if double_list[i+1] != 0:
                    record += ' + '
            elif i == len(double_list) - 2 and double_list[i] != 0:
                record += f'{double_list[i]}x'
                if double_list[i+1] != 0:
                    record += ' + '
            elif i == len(double_list) - 1 and double_list[i] != 0:
                record += f'{double_list[i]} = 0'
            elif i == len(double_list) - 1 and double_list[i] == 0:
                record += ' = 0'
    return record


value = int(input("Введите степень "))
new_file(new_text(subsequence(value)))