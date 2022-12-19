# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input("Введите число  ")
# result = 0
# for i in number:
#     result+= int(i)
#     print(result)



# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def mult(n):
#     if n == 1:
#         return 1
#     else:
#         return n * mult(n - 1) # небольшая рекурсия
# number = int(input("Введите число: "))
# list = []
# for e in range(1, number + 1):
#     list.append(mult(e))
# print(f"Произведения чисел от 1 до {number}:  {list}")



# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06

# n = int(input('Введите число: '))
# sum = 0
# list = []
# for i in range(1, n + 1):
#     num = (1 + 1 / i) ** i
#     num = round(num, 2)
#     list.append(num)
#     sum += num
# print(f'n = {n} -> {list}\nСумма {round(sum, 2)}')


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.


# Создаем список рандомно:
# import random
# n = int(input('Введите количество элементов списка: '))
# value_min = int(input('Введите минимальный элемент списка: '))
# value_max = int(input('Введите максимальный элемент списка: '))
# first_list = [random.randint(value_min, value_max) for _ in range(n)]

# не совсем понял идею "Позиции хранятся в файле file.txt в одной строке одно число".

# перемешиваие списка 
# second_list = first_list.copy()
# for i in range(len(second_list)):
#     j = random.randint(0, (len(second_list) - 1))
#     if i != j:
#         second_list[i], second_list[j] = second_list[j], second_list[i]
# print(f'Созданный список: {first_list}')
# print(f'Перемешанный список: {second_list}')