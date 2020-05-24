import timeit
import cProfile

a = [i for i in range(100)]

# у списка линейная асимптотика, но нам нужно научиться
# оценивать алгоритм, для этого есть timeit.

print(timeit.timeit('a = [i for i in range(100)]'))

# код был запущет 1 000 000 раз и это заняло примерно 4 сек.
# тут мы делаем 1 замер и по нему пытаемся оценить асимптотику.
# Для реальной оценки нужно минимум 3 замера, а лучше больше.

print(timeit.timeit('a = [i for i in range(10)]', number=100))
print(timeit.timeit('a = [i for i in range(100)]', number=100))
print(timeit.timeit('a = [i for i in range(1000)]', number=100))
print(timeit.timeit('a = [i for i in range(10000)]', number=100))

# итак мы получили примерно линейную асимптотику - при увеличении количества данных
# увеличивается время обработки (в 10 раз данные - в 10 раз время).
# нужно оценивать не абсолютные значения времени, а то как меняется время
# обработки при увеличении количества данных на входе.

# при увеличении количества повторений будет неправильное измерение, т.к.
# зависимость всегда будет линейной в таком случае.

def get_len(lst):
    return len(lst)

def get_sum(lst):
    sum_ = 0
    for item in lst:
        sum_ += item
    return sum_

def main(n):
    array = [i for i in range(n)]
    len_ = get_len(array)
    sum_ = get_sum(array)

cProfile.run('main(100000)')

# итак, мы получили таблицу, которая показывает
# сProfile анализирует код и показывает сколько выполнятся каждая часть кода.
# он служит для поиска слабых мест в коде. Время он показывает округленно.
# timeit - нужно для оценки времени работы алгоритма.

# percall - время работы на один вызов (если кусочки кода вызываются более 1 раза)
# cumtime - накопительное время при выполнении программы.

# данный инструмент говорит что больше всего времени тратит ф. для подсчета суммы.
# находим самое слабое звено и пытаемся его оптимизировать.

# числа Фибоначчи:

0, 1, 1, 2, 3, 5, 8, 13, 21

# итак, напишем тестирующую функцию:

import timeit
import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    for i, item in enumerate(lst):
        assert item == func(i)  # если утверждение не верно, кидает исключение.
        print(f'Test {i} OK')

# поиск числа Фибоначчи простой рекурс вариант.

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# убедимся что это работает:
test_fib(fib) # передали саму функцию.

print(timeit.timeit('fib(2)', number=100, globals=globals()))   # сюда пищем замеры.
print(timeit.timeit('fib(4)', number=100, globals=globals()))   # небольшой вывод на что похожа асимптотика.
print(timeit.timeit('fib(8)', number=100, globals=globals()))
print(timeit.timeit('fib(16)', number=100, globals=globals()))

# асимптотика О(n!) видим по цифрам.
# (чтобы найти число, мы 2 раза вызываем ф. рекурсивно, а она вызывает в раза предыдущие)

cProfile.run('fib(2)')
cProfile.run('fib(4)')
cProfile.run('fib(8)')
cProfile.run('fib(16)')

# видим, что для поиска второго числа, ф. вызвала сама себя 3 раза.
# 4е число 9 вызовов.
# 8е число 67 раз.
# 16е число - 3193 раза, не было переполнения стэка (по умолч 1000 вызовов).
# потому что рекурс ф. попадала на стэк и снималась со стэка, одновременно не было более 1000 вызовов. Одноавременно было
# макс 16 вызовов стэка.

# Рекурсия + словарь = мемоизация.

def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:    # если значение в словаре есть, возвращаем его.
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)  # если нет, то помещаем в словарь.
        return fib_d[n]   # и возвращаем значение

    return _fib_dict(n)

# убедимся что ф. хорошо считает:

test_fib(fib_dict)

print(timeit.timeit('fib_dict(2)', number=100, globals=globals()))
print(timeit.timeit('fib_dict(4)', number=100, globals=globals()))
print(timeit.timeit('fib_dict(8)', number=100, globals=globals()))
print(timeit.timeit('fib_dict(16)', number=100, globals=globals()))

# считает намного быстрее! вариант линейный, при увеличении в 2 раза, данных,
# время также растет в 2 раза.

cProfile.run('fib_dict(2)')
cProfile.run('fib_dict(4)')
cProfile.run('fib_dict(8)')

# основная ф. вызыв 1 раз, в внутр. 2n - 1 раз.
# также видна линейная асимптотика.

# Еще одна реализация циклом.

def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(n):
        first, second = second, first + second
    return first

test_fib(fib_loop)

# замерим:

print(timeit.timeit('fib_loop(2)', number=100, globals=globals()))
print(timeit.timeit('fib_loop(4)', number=100, globals=globals()))
print(timeit.timeit('fib_loop(8)', number=100, globals=globals()))
print(timeit.timeit('fib_loop(16)', number=100, globals=globals()))
print(timeit.timeit('fib_loop(32)', number=100, globals=globals()))
print(timeit.timeit('fib_loop(64)', number=100, globals=globals()))

# асимтотика примерно как n^2.

cProfile.run('fib_loop(16)')

# ничего нет интересного, очень простая ф.

import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# кэширует результат выполнения ф. и при следующем вызове просто выдает
# его же, а не вычисляет заново. Поэтому при запуска 100 раз во время
# теста получается очень быстро, но не показательно.
