# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_n = 0
max_number = 0

for number in array:
    n = array.count(number)
    if n > max_n:
        max_n = n
        max_number = number

array.remove(max_number)   # удаляем один из элементов, которые встречались чаще всего, чтобы узнать есть ли еще такие
                           # элементы.

for number in array:
    n = array.count(number)
    if n == max_n:
        print('Более одного элемента встречается чаще всего. Один из них приведен ниже:')
        break

print(f'В массиве {max_number} встречается чаще всего.')