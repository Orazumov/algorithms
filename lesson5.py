# урок восвящен модуля collections.
# коллекции - например последовательности:
# изменяемые - list (массивы)
# неизменяемые кортеж, строка (массивы)

# бывают множества - set / frozenset.
# нельзя обратиться по индексу, элементы не могут повторяться.

# словари - пара ключ/значение. Ключи уникальны, значения могут повт.

# на самом деле коллеций больше, чем это количество. в др. языках
# эти др. коллекции лежат на поверхности.

# есть модуль collections, где они лежат.

# Стэк - как стопка подносов на столе, брать подносы можно только
# сверху. Класть тоже можно только сверху на стопку.

# в Питоне поместить элемент - это .append()
# взять - это .pop()
# проверить глубину стэка - это len()
# все это для списка list.

# т.е. если использовать эти команды к списку, то это и есть стэк.

# FIFO / LIFO.

from collections import Counter

# Counter - мультимножество. Продвинутая версия словаря.

a = Counter()
b = Counter('abrakadabra')   # просеится и запишется сколько раз встречается каждя буква.
c = Counter({'red': 10, 'green': 15})
print(a, b, c, sep='\n')

print(b['z'])
# если был бы обычный словарь, была бы ошибка - ключа z нет.
# мультимножество выдаст 0

b['z'] = 3

print(b)

# ключ z расположился между a и b, т.е. элементы упорядочены по весу.
# что чаще встречается.

print(b.most_common(3))

# скажи 3 элемента, которые встречаются максимально часто.

# при распечатке b и r одинакового веса, но они располагаются по
# принципу кто раньше попал в коллекцию, тот и раньше.

x = Counter(a=3, b=-2, c=4)
y = Counter(a=2, b=4, c=-2)

print(x + y)

# суммируем значения ключей.

x = Counter(a=3, b=-2, c=1)
y = Counter(a=2, b=4, c=-2)

print(x + y)

#  с исчез, т.к. его значение -1, меньше 0. если 0 - тоже исчезает.
# но в ручную можно добавить элемент -1.

print(x - y)

# аналогично можно вычитать.  * и / не работает.

print(x & y)  # - логическое И

# И там и там встречается a 2 раза -> a:2 другие не встречаются там и там

print(x | y)  # логическое ИЛИ

# берем по максмуму - максимальное из двух чисел.

from collections import OrderedDict

# pythin 3.5 и ранее: dict()  -> если пробегаем по нему for - случайный порядок выдачи.
# поэтому использовали OrderedDict - элементы выводятся в том порядка в каком заданы.
# в версии 3.6 : di# ct() == OrderedDict стали вести себя одинаково. Как ввели значения, так они и выводятся.
# python 3.7 и позднее: dict()  закрепился порядок.  Поэтому OrderedDict стал бесполезным.

# таким образом если в коде есть OrderedDict, значит код был написан ранее чем 3.5 версия Питона.


from collections import defaultdict

a = defaultdict()
print(a)

# в этом случае никаких плюшек нет.
# а если на вход передать ф, то она будет определять его поведение.

text = 'gregergreg ergergergreg43gq[wpfk'

b = defaultdict(int)

for char in text:
    b[char] += 1

print(b)

# для не сущ. ключей вызывается ф.
# в итоге посчитается сколько раз встречается каждая буква.
# в данном случае значение словаря - int.

# по умолчанию int возвращает 0, в итоге получается b[char] = 0 потом += 1

# то есть значение ключа g по умолчанию = 0 (св-во defaultdict), но потом, когда буква встречается, мы увеличиваем
# значение, происвоенное ключу на 1. Если встречается второй раз, то еще раз на 1 и т.д.

# таким образом считается буква в строке если она встретилась 1 раз.

c = defaultdict(list)

c[animal].append(distance)

# теперь к значению ключа можно обращаться как к списку.

# еще пример:

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)

print(d)

# В итоге мы получим в качестве ключей словаря - первые значения в кортежах, а в качестве значений - списки, которые относятся
# к данным ключам. Без defaultdict пришлось бы писать if else - в каком то случае присваивать значение, а в каком-то
# добавлять новое в список.
# Т.е. значение - изначально список!

from collections import deque

# очередь.

# в очереди есть голова, элементы и последовательные ссылки на следующий
# элемент и предыдущий. последний - хвост.

# это и есть настоящий список.

a = deque()
b = deque('abrakadabra')
print(a, b, sep='\n')

# нужно выбирать соответствуюшие методы к массиву и списку.

c = deque([1, 2, 3, 4])
print(c)
c.append(5)

# получаем 12345 добавился элемент в конец очереди.

c.appendleft(6)

# 612345

# это работает быстро!

c.extend([7, 8])

# 61234578

c.extendleft([9, 10])

# 10 9 61234578    добавили девятку слева, потом десятку левее девятки.

# очереди преобразование - сложность O(n)

spam = c.pop()

# spam = 8

eggs = c.popleft()

#eggs = 10

# append, appendleft, extend, extendleft - константная сложность О(контстанта)
# если был быб список list - то appendleft О(n), extendleft - O(n)*n
# popleft - аналогично.

# очередь быстрее во всем кроме

print(c[2])  # - медленнее, очередь проходит по всей очереди начиная с начала - О(n).

d = [1, 2, 3]
print(d)
print(d[::-1])  # разворачивает справа налево. О(n).
# нужно пройти минимум половину списка и поменять значения местами.

c.reverse()
print(c)  # разворот очереди мгновенно!
# меняются местами голова и хвост.

с = deque([1, 2, 3, 4, 5], maxlen=5)

# если добавить 1 элемент слева, то выдавится один справа.

# преобразование одной структура данных в другую - это линейная операция. О(n).

from collections import namedtuple

# именованный кортеж.

class Person:
    def __init__(self, name, race, health, mana, armor):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.armor = armor

    def __str__(self):
        return f'name = {self.name}'

hero = Person('Aaz', 'Izverg', 300, 0, 50)

print(hero.name)
print(hero)  # выдается только объект <__main__.Person object at 0x043214>
# перепишем __str__

# вместо этого можно так:

PersonNew = namedtuple('PersonNew', 'name, race, health, mana, armor')
# в начале обязательно название класса. потом параметры.
# потому что интерпретатор выполняет сначала то что справа, потом что слева,
# чтобы назывался класс одинаково, как и слева.

hero_new = PersonNew('Aaz', 'Izverg', 300, 0, 50)
print(hero_new.name)
print(hero_new)

hero_new.mana = 100
print(hero_new)

# помеять не можем, потому что это КОРТЕЖ.

# но можно сделать такую фишку:

hero_new = hero_new._replace(mana=100)
# сработало, теперь создалась копия кортежа с новым параметром.



