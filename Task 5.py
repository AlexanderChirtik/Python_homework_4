# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов

with open('polynomial_1.txt', 'w') as data:
    data.write('34x^3 + 18x^2 + 78x + 84 = 0')

with open('polynomial_2.txt', 'w') as data:
    data.write('79x^4 + 95x^3 + 25x^2 + 95x + 45 = 0')

with open('polynomial_1.txt','r') as data:
    polynomial_1 = data.readline()
    list1 = polynomial_1.split()

with open('polynomial_2.txt','r') as data:
    polynomial_2 = data.readline()
    list2 = polynomial_2.split()

with open('sum_polynomials.txt', 'w') as data:
    data.write(f'{list1} + {list2}')