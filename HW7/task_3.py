from random import randint

SIZE = 10
ACT_SIZE = 2*SIZE + 1
array = [randint(-100, 99) for _ in range(ACT_SIZE)]
print(f'Массив до сортировки гномиками: {array}')

i = 0
j = 0

while i < len(array):
    if i == 0 or array[i-1] < array[i]:
        if j > i:
            i = j
        i += 1
    else:
        array[i-1], array[i] = array[i], array[i-1]
        if i > j:
            j = i
        i -= 1

print(f'Массив после сортировки: {array}')
print(f'Медиана массива: {array[len(array)//2]}')
