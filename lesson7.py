# Урок номер 7.

# алгоритмы сортировки.

# Сортировку можно разбить на 3 части: сравнение, перестановка,

# Сортировка пузырьком.

import random

array = [i for i in range(10)]

print(array)

random.shuffle(array)   # случайная сортировка - перемешали
# можно конечно мешать пока элементы не встанут на свои места это O(n*n!)
print(array)

# Пузырек - берем пару соседних элементов, смотрим кто больше,
# и меняем их местами.
# В итоге большее число движется к концу.

n = 1

while n < len(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    n += 1
    print(array)   # смотрим промежуточные значения

print(array)

# сложность O(n^2) сортировка считается устойчивой.
# т.е. одинаковые элементы в массиве сохранят свой порядок.

# Сортировка выбором.

def selection_sort(arr):

    for i in range(len(array)):
        idx_min = i
            for j in range(i + 1, len(array)):
                if arr[j] < arr[idx_min]:
                    idx_min = j
            arr[idx_min], arr[i] = arr[i], arr[idx_min]
            print(arr)

# массив изменяемая структура, поэтому поменяв ее в ф. он меняется и сверху.
# выбираем первый слева элемент и сравниваем ее со всем что есть, а потом проходимся по массиву и ищем самую маленькую цифру.
# ставим ее левее всего.
# неустойчивая. тоже О(n^2)

selection_sort(array)
print(array)

# сортировка вставками:

def insertion_sort(arr):
    for i in range(1, len(arr)):  # 0 элемент упорядочен
        spam = arr[i]
        j = i
        while arr[j-1] > spam and j > 0:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = spam
        print(arr)

# массив как книжная полка. если в массиве 5 элемент, то он упорядочек.
# вытягием следующую цифру - сравниваем. Если он больше - ставим обратно.
# и так далее пока не встретим ту цифру, кот меньше. Тогда вставляем ее в левую отсорт часть, чтобы она все еще было отсортир.
# O(n^2) сложность.

# быстрая сортировка.
# сложность О(n*log n)

# рекурсивный.

def quick_sort(arr, first, last):
    print(arr[first:last+1])
    if first >= last:
        return
    pivot = arr[random.randint(first, last)]
    i = first
    j = last

    while i <=j:
        while arr[i] < pivot:      # слева есть кто-то большой, мы его вычислили
            i += 1
        while arr[j] > pivot:      # справа есть маленький, мы его вычислили
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quick_sort(arr, first, j)
    quick_sort(arr, i, last)


quick_sort(array, 0, len(array)-1)

# самом худшем случае О(n^2), в среднем О(n * log n)

# алгоритм сортировки Шелла.

def shell(arr):
    assert len(arr) < 4000, 'Массив слишком большой'

    def new_increment(arr):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(arr) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(arr):
        for i in range(increment, len(arr)):
            for j in range(i, increment - 1, -increment):
                if arr[j - increment] <= arr[j]:
                    break
                arr[j], arr[j - increment] = arr[j-increment], arr[j]

# сортировка Тима Питерса.

# массив разделается на блоки, внутри сорт вставками, а затем объединяем сортировкой слиянием.
# устойчивая сортировка.
# это и есть sorted

from collections import namedtuple

Person = namedtuple('Person', 'name age')

p_1 = Person('Sam', 31)
p_2 = Person('John', 56)
p_3 = Person('Sum', 41)
p_4 = Person('Ezra', 66)
p_5 = Person('Clint', 90)

people = [p_1, p_2, p_3, p_4, p_5]

a = sorted(people)
print(a)

# если бы мы написал класс, то не получилось бы отсортировать так.
# отсортировалось по первому значению - имени.

from operator import attrgetter

b = sorted(people, key=attrgetter('age'))

print(b)

# отсортировали теперь по возрасту.

# если нужно отсортировать по нескольким характеристикам, можно сортировать так несколько раз с разными ключами.

a = sorted(people, key=attrgetter('Отчество'))
b = sorted(a, key=attrgetter('Имя'))
c = sorted(b, key=attrgetter('Фамилия'))







