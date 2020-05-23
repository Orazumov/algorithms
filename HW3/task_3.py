#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = array[0]
min_ = array[0]
maxInd = 0
minInd = 0

for i in range(len(array)):
    if array[i] > max_:
        max_ = array[i]
        maxInd = i
    if array[i] < min_:
        min_ = array[i]
        minInd = i

array[maxInd], array[minInd] = array[minInd], array[maxInd]

print(f'Поменяли максимальный {max_} и минимальный {min_} элемент местами: {array}')