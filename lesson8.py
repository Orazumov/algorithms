# Деревья и хэш функции.

# Двоичные деревья поиска.

# В дереве есть узлы и ребра.
# Узел в самом верху - корень. Всегда 1.
# Ребра из него выходят, но не входят в него.
# Узлы в низу - это листья. Их обычно много.
# Наоборот - ребра входят в листья, но не выходят из них.
# Деревно двоичное если из узлов выходят не более 2х ребер.

# Деревья рекурсивные.

# Есть родительские и дочерние узлы.
# Корень - только родительский, листья - только дочерние.
# Если у каждого узла - 2 дочерних, дерево - полное.
# Если все узлы на одной высоте, то дерево - идеальное.
# (ряды узлов по одной линии).

# Поисковое дерево - все что находится слева от любого узла меньше, справа - больше.

# Дерево - еще одна коллекция для хранения данных.

# Если дерево вырожденное:
# *-->*-->*-->* - это односвязанный список.

# Это класс узел:

class myNode:
    def __init__(self, value, left = None, right=None):
        self.value = value
        self.left = left
        self.right = right

# в переменной value - значение в узле
# left, right - указание на узлы слева и справа.

# учебная библиотека:
# нужно ее установить отдельно pip install..

from binarytree import tree, bst, Node

a = tree(height=4, is_perfect=True)
print(a)

# демонстрируем дерево. высота его - количество ребер от корня до самого нижнего листа.

b = bst(height=4, is_perfect=False)
# бинарное поисковое дерево.
print(b)

# Строим свое дерево руками:
c = Node(13)
c.left = Node(7)
c.right = Node(23)
c.left.left = Node(0)
c.right.left = Node(5)

print(c)

# видим свое дерево.

# так неверно:
c.left.right = 22
# тк. 22 - это int а не узел

# заменим на MyNode:
c = MyNode(13)
c.left = MyNode(7)
c.right = MyNode(23)
c.left.left = MyNode(0)
c.right.left = MyNode(5)

print(c)

# ошибки нет, выдается просто объект - проблема только с выводом.
# учебная библиотека хранит только числа, а мы можем хранить все что угодно.


class myNode:
    def __init__(self, value, left=None, right=None, data=None):
        self.value = value
        self.left = left
        self.right = right
        self.data = data

# можно добавить любые данные!

# ф. поиска по дереву:
bt = bst(height=5, is_perfect=True)

print(bt)
num = int(input('Что найти: '))

def search(bin_tree, number, path=''):
    if bin_tree.value == number:
        return f'Число {number} нахожится по пути:\nКорень{path}'
    if number < bin_tree.value and bin_tree.left is not None: # None - чтобы это был не лист. Дерево поисковое!
        return search(bin_tree.left, number, path=f'{path}\nшаг влево')
    if number > bin_tree.value and bin_tree.right is not None: # None - чтобы это был не лист. Дерево поисковое!
        return search(bin_tree.right, number, path=f'{path}\nшаг вправо')
#   когда у нас слева и справа None - значит мы дошли до листьев, числа нет в дереве.
    return f'Число {number} отсутсвует'

print(search(bt, num))

# алгоритм Хаффмана - дерево, которое позволяет хранить данные.
# и сжимать информацию.

# берем строку, считаем частоту символов в строке.
# создаем коллекцию, упорядочиваем ее.
# формируем дерево.
# идем по дереву - если влево то 0, вправо - 1.
# запоминаем как кодировать каждый символ в листе дерева.
# получаем таблицу:
# 'b' 00
# 'e' 101
# ..

# Хэширование.

# Для сжатия информации, но разжать ее нельзя.

h_list = [None] * 26

# напишем свою хэш ф.
def my_hash(value):
    h_index = ord(value[0]) - ord('a')
    h_list[h_index] = value
    print(h_list)

a = 'apple'
my_hash(a)
# захэшировали яблоко, поместили в нулевую ячейку


b = 'banana'
my_hash(b)
# банан.

с = 'apticot'
my_hash(c)
# яблоко стерлось! хэш коллизия.
# хорошая хэш ф. не допускает коллизий.

print(4567 == 4*10**3 + 5*10**2 + 6*10*1 + 7*10**0)
# True так и есть.
# позиционная система, цифра имеет свой вес.

# Воспользуемся и напишем другую хэш ф.

def my_hash2(value):
    letter = 26
    h_index = 0
    for i, char in enumerate(value):
        h_index +=(ord(char) - ord('a') + 1) * letter **i
        # аналогичная позиционная система для букв.
    return h_index

print(my_hash2(a))
print(my_hash2(b))
print(my_hash2(c))

# Все слова имею свой хэш, нет коллизий
# тут проблема в том что возвращается не одинаковое число цифр.

def my_hash2(value):
    letter = 26
    h_index = 0
    size = 10_000
    for i, char in enumerate(value):
        h_index += (ord(char) - ord('a') + 1) * letter **i
        # аналогичная позиционная система для букв.
    return h_index % size

# чтобы не было коллизий нужно, чтобы size был 2*n - количетсво символов, которые хэшируем.

# встроенная ф. хэш:

s = 'ferferfre'
print(hash(s))
print(hash(s))
print(hash(s))
print(hash(s))
print(hash(s))

# запускаем несколько раз, значения одинаковые, но каждый раз разные.
# хэш считается от момента запуска до момента остановки программы.
# поэтому если важно сохранение хэш для длительного использования, то берем:

import hashlib

print(hashlib.sha1('Hello world!'))
# ошибка - нужен Unicode
print(hashlib.sha1(b'Hello world!'))
# это не текст, а байты.
print(hashlib.sha1(b'Hello world!ж'))
# ошибка - ж отсутствует в таблице ASCII

# поэтому делаем так:

print(hashlib.sha1(b'Hello world!ж'.encode('utf-8')))

# вроде норм, но есть грабли:

a = hashlib.sha1('Hello world!ж'.encode('utf-8'))
b = hashlib.sha1('Hello world!ж'.encode('utf-8'))

print(a == b)

# False, т.к. вернулся объект в памяти, а не представление хэша, поэтому:

a = hashlib.sha1('Hello world!ж'.encode('utf-8')).hexdigest()
b = hashlib.sha1('Hello world!ж'.encode('utf-8')).hexdigest()

print(a == b)
# теперь труе. Таким образом у нас останется хэш и можно будет например проверять пароль


