#Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

#Первый — с помощью алгоритма «Решето Эратосфена».
#Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

#Второй — без использования «Решета Эратосфена».
#Примечание. Вспомните классический способ проверки числа на простоту.

import timeit
import cProfile

def simple_number_sieve(number):

    n = 100
    while True:
        sieve = [i for i in range(n)]

        sieve[1] = 0

        for i in range(2, n):
            if sieve[i] != 0:
                j = i + i
                while j < n:
                    sieve[j] = 0
                    j += i

        res = [i for i in sieve if i != 0]

        if number > len(res):
            n = n * 10
            continue
        else:
            result = res[number-1]
            break
    return result

def simple_number_naive(number):

    lst = []
    i = 2
    while True:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
        if len(lst) == number:
            return lst.pop()
        i += 1

number = int(input('Введите номер простого числа: '))

print(f'Ответ решето: {simple_number_sieve(number)}')

print(f'Ответ наивный алгоритм: {simple_number_naive(number)}')

print(timeit.timeit('simple_number_sieve(10)', number=100, globals=globals()))   # 0.0036937999999999693
print(timeit.timeit('simple_number_sieve(100)', number=100, globals=globals()))   # 0.04857339999999999
print(timeit.timeit('simple_number_sieve(500)', number=100, globals=globals()))   # 0.5563921000000001
print(timeit.timeit('simple_number_sieve(1000)', number=100, globals=globals()))   # 0.5510775999999997


cProfile.run('simple_number_sieve(10)')
cProfile.run('simple_number_sieve(100)')
cProfile.run('simple_number_sieve(500)')
cProfile.run('simple_number_sieve(1000)')

#         1    0.004    0.004    0.005    0.005 task_2.py:13(simple_number_sieve)
#         3    0.001    0.000    0.001    0.000 task_2.py:17(<listcomp>)
#         3    0.001    0.000    0.001    0.000 task_2.py:28(<listcomp>)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.len}

print(timeit.timeit('simple_number_naive(10)', number=100, globals=globals()))   # 0.0025712000000002178
print(timeit.timeit('simple_number_naive(100)', number=100, globals=globals()))   # 0.23263919999999993
print(timeit.timeit('simple_number_naive(500)', number=100, globals=globals()))   # 8.3964015
print(timeit.timeit('simple_number_naive(1000)', number=100, globals=globals()))   # 39.171698400000004

# Эратосфен явно быстрее!

cProfile.run('simple_number_naive(10)')
cProfile.run('simple_number_naive(100)')
cProfile.run('simple_number_naive(500)')
cProfile.run('simple_number_naive(1000)')

#        1    0.383    0.383    0.385    0.385 task_2.py:38(simple_number_naive)
#        1    0.000    0.000    0.385    0.385 {built-in method builtins.exec}
#     7918    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}