'''4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.'''
# def square(a):
#     b = 4 * a
#     c = a * a
#     d = round((2 ** 0.5) * a)
#     return (b, c, d)
# a = int(input('Введи целое число: '))
# print(square(a))
#
# # variant from teacher
# a = int(input('Введи целое число: '))
# print((4 * a, a * a, round(a * (2 ** 0.5))))


'''4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35
	position: web developer'''

# my_dict = {
# 'name': 'John',
# 'last_name': 'Smith',
# 'age': 35,
# 'position': 'web developer'}
# def task_2(**kwargs):
#     print(*kwargs.items(), sep='\n')
#
# task_2(name='John', last_name='Smith', age=35, position='web developer')

'''4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     положительные числа'''
# my_list = [20, -3, 15, 2, -1, -21]
# result = list(filter(lambda x: x > 0, my_list))
# print(result)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# result_2 = reduce(lambda x, y: x * y, my_list)
# print(result_2)


# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# import time
# def timer(f):
#     def tmp(*args, **kwargs):
#         t = time.perf_counter()
#         res = f(*args, **kwargs)
#         print(time.perf_counter())
#         return res
#
#     return tmp
# @timer
# def func(x, y):
#     return x + y
#
# func(1, 2)

'''4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле. '''

from my_calc import sum
from my_calc import sub
from my_calc import mult
from my_calc import div

# var2 -  можно вызвать все фунукции сразу:
from my_calc import *


# a = int(input('Введи число: '))
# b = int(input('Введи число: '))
#
# print(sum(a, b))
# print(sub(a, b))
# print(mult(a, b))
# print(div(a, b))

