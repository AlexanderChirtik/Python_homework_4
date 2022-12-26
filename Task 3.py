#Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
numbers = input("Введите числа ").split()
for i in range(0, len(numbers)):
    if (numbers.count(numbers[i]) == 1):
        print(numbers[i], end=" ")
