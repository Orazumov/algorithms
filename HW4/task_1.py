# выбираем интересную задачу из первых трех уроков. где есть изм. значение n и оценивать
# асимптотику.
# написать 3 варианта ее решения.
# оцениваем через timeit и cProfile + комментарии результаты.
# вывод о том на какую асимптотику похож алгоритм.

# вариант с рекурсией:

import timeit
import cProfile
import random

import sys
sys.setrecursionlimit(10000)        # увеличим стек.

# сгенерируем случайный цифры для тестирования типа int и типа str:

def generate_int(SIZE, MIN_ITEM = 0, MAX_ITEM = 9):

    array = [str(random.randint(MIN_ITEM, MAX_ITEM)) for _ in range(SIZE)]
    return int(''.join(array))

number1 = generate_int(10)
number2 = generate_int(100)
number3 = generate_int(500)
number4 = generate_int(1000)

def generate_str(SIZE, MIN_ITEM = 0, MAX_ITEM = 9):

    array = [str(random.randint(MIN_ITEM, MAX_ITEM)) for _ in range(SIZE)]
    return ''.join(array)

str1 = generate_str(10)
str2 = generate_str(100)
str3 = generate_str(500)
str4 = generate_str(1000)

def count_numbers_recurs(num, even_num=0, odd_num=0):
    if num == 0:
        return f'Четных цифр {even_num}, Нечетных цифр {odd_num}'
    if num % 10 % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    return count_numbers_recurs(num // 10, even_num, odd_num)

print(timeit.timeit('count_numbers_recurs(number1)', number=1000, globals=globals()))   # 0.004599900000000004
print(timeit.timeit('count_numbers_recurs(number2)', number=1000, globals=globals()))   # 0.0557932
print(timeit.timeit('count_numbers_recurs(number3)', number=1000, globals=globals()))   # 0.5847325999999999
print(timeit.timeit('count_numbers_recurs(number4)', number=1000, globals=globals()))   # 2.0261818000000003

# напоминает O(n!)

cProfile.run('count_numbers_recurs(number1)')  # 11/1    0.000    0.000    0.000    0.000 task_1.py:26(count_numbers_recurs)
cProfile.run('count_numbers_recurs(number2)')  # 101/1    0.000    0.000    0.000    0.000 task_1.py:26(count_numbers_recurs)
cProfile.run('count_numbers_recurs(number3)')  # 501/1    0.001    0.000    0.001    0.001 task_1.py:37(count_numbers_recurs)
cProfile.run('count_numbers_recurs(number4)')  # 1001/1    0.003    0.000    0.003    0.003 task_1.py:37(count_numbers_recurs)


# Вариант с циклом:

def count_numbers_cycle(num):
    even = 0
    odd = 0
    for i in num:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return f'Четных цифр {even}, Нечетных цифр {odd}'

print(timeit.timeit('count_numbers_cycle(str1)', number=1000, globals=globals()))   # 0.004092900000000066
print(timeit.timeit('count_numbers_cycle(str2)', number=1000, globals=globals()))   # 0.03146570000000004
print(timeit.timeit('count_numbers_cycle(str3)', number=1000, globals=globals()))   # 0.15148390000000012
print(timeit.timeit('count_numbers_cycle(str4)', number=1000, globals=globals()))   # 0.35244359999999997

# напоминает O(n^2)

cProfile.run('count_numbers_cycle(str1)')  # 1    0.000    0.000    0.000    0.000 task_1.py:57(count_numbers_cycle)
cProfile.run('count_numbers_cycle(str2)')  # 1    0.000    0.000    0.000    0.000 task_1.py:57(count_numbers_cycle)
cProfile.run('count_numbers_cycle(str3)')  # 1    0.000    0.000    0.000    0.000 task_1.py:57(count_numbers_cycle)
cProfile.run('count_numbers_cycle(str4)')  # 1    0.000    0.000    0.000    0.000 task_1.py:57(count_numbers_cycle)



# вариант с массивом:

def count_numbers_list(num):
    even = []
    odd = []
    for i in num:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return f'Четных цифр {len(even)}, Нечетных цифр {len(odd)}'

print(timeit.timeit('count_numbers_list(str1)', number=1000, globals=globals()))   # 0.004632899999999829
print(timeit.timeit('count_numbers_list(str2)', number=1000, globals=globals()))   # 0.03553050000000013
print(timeit.timeit('count_numbers_list(str3)', number=1000, globals=globals()))   # 0.1758829999999998
print(timeit.timeit('count_numbers_list(str4)', number=1000, globals=globals()))   # 0.35385430000000007

# напоминает также O(n^2), видимо функции append и len не вносят заметного вклада.

cProfile.run('count_numbers_list(str1)')  #         1    0.000    0.000    0.000    0.000 task_1.py:81(count_numbers_list)
                                          #         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
                                          #         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                                          #         10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('count_numbers_list(str2)')  #         1    0.000    0.000    0.000    0.000 task_1.py:83(count_numbers_list)
                                          #         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
                                          #         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                                          #         100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('count_numbers_list(str3)')  #         1    0.000    0.000    0.000    0.000 task_1.py:83(count_numbers_list)
                                          #         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
                                          #         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                                          #         500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('count_numbers_list(str4)')  #         1    0.000    0.000    0.001    0.001 task_1.py:83(count_numbers_list)
                                          #         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
                                          #         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                                          #         1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

