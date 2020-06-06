from random import randint

SIZE = 10
array = [randint(-100, 99) for _ in range(SIZE)]
print(f'Массив до сортировки пузырьком: {array}')

def bubble(array):
    n = 1

    while n < len(array):
        for i in range(len(array) - n):     # каждый раз при последующем проходе не нужно идти до конца массива, т.к.
            if array[i] < array[i + 1]:     # последний элемент уже отсортирован.
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array

print(f'Массив после сортировки: {bubble(array)}')
