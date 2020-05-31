#Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
#● написать 3 варианта кода (один у вас уже есть);
#● проанализировать 3 варианта и выбрать оптимальный;
#● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
#● написать общий вывод: какой из трёх вариантов лучше и почему.

from functools import reduce
from sys import getsizeof

def append_to_lst(*args):
    variables = []
    for item in args:
        variables.append(item)
    return variables

variables = []     # массив для оценки памяти

n = int(input('Введите количество элементов ряда чисел: '))

summ = 1
number = 1

for i in range(1, n + 1):

    number = number / 2

    if i % 2 == 0:
        summ = summ + number
    else:
        summ = summ - number

print(f'Ответ вариант 1: {summ}')

variables = append_to_lst(summ, i, n, number)

memory_size = int()

for i in variables:
    memory_size += getsizeof(i)
print(f'Вариант 1 занял в памяти: {memory_size} байт.')

# вариант через рекурсию:

variables = []

def summa(n, summ = 1.0, number = 1.0, i = 1):

    if i == n:
        return summ
    number = number / 2
    if i % 2 == 0:
        summ = summ + number
    else:
        summ = summ - number

    variables.append(summa)

    return summa(n, summ, number, i+1)

print(f'Ответ вариант 2: {summa(n)}')

memory_size = float()
for i in variables:
    memory_size += getsizeof(i)
print(f'Вариант 2 занял в памяти: {memory_size} байт.')

# вариант со списком:


variables = []     # массив для оценки памяти

lst = [1]
number = 1

for i in range(1, n + 1):

    number = number / 2

    if i % 2 == 0:
        lst.append(number)
    else:
        lst.append(-number)

answer = reduce(lambda x, y: x+y, lst)
print(f'Ответ вариант 3: {answer}')

def show_lst_float_int(object, mem_size = 0):

    if isinstance(object, int) or isinstance(object, float):
        return getsizeof(object)

    mem_size += getsizeof(object)

    if isinstance(object, list):
        for item in object:
            mem_size += getsizeof(item)
        return mem_size

variables = append_to_lst(lst, answer, i, n, number)

memory_size = int()
for i in variables:
    memory_size += show_lst_float_int(i)
print(f'Вариант 3 занял в памяти: {memory_size} байт.')