#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

value = int(input("Введите натуральное число "))
while (value > 1):
     for i in 2, 3, 5, 7, value:
         if (value % i == 0):
            print(i, end=' ')
            value /= i
            break