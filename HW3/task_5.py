# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к
# задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative = float('-inf')   # изначально - минус бесконечность.

for number in array:
    if number < 0:
        if number > max_negative:
            max_negative = number

print(f'Максимальный отрицательный номер в массиве: {max_negative}')
