#Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
#элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
#соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

def align(a_number, b_number):                  # добавляем слева лишние нули, чтобы сделать 2 числа равными по длине.

    if len(a_number) > len(b_number):
        difference = ['0' for _ in range(len(a_number) - len(b_number))]

        b_number.extendleft(difference)
    elif len(b_number) > len(a_number):
        difference = ['0' for _ in range(len(b_number) - len(a_number))]

        a_number.extendleft(difference)

    return a_number, b_number

def summ(a, b):             # суммируем 2 отдельно взятых числа, оказавшихся друг под другом.

    return (int(a, 16) + int(b, 16))

def next_count(number):     # рассчитываем какое число перенести на следующий разряд и какое записать в текущий.

    count = 0

    while number >= 16:
        number = number - 16
        count += 1

    return number, count

def normalize(result):      # нормализуем полученное ниже значение при сложении - приводим к тому, что каждое число < 16ти..

    result_out = deque()
    position = 1
    result.reverse()

    for number in result:

        if not result_out:         # если у нас перввый элемент, в выходной очереди - ничего.
            if number >= 16:
                number_, count = next_count(number)
                result_out.appendleft(number_)
                result_out.appendleft(count)
            else:
                result_out.appendleft(number)
        else:
            if len(result_out) == position:     # если не первый элемент и в прошлый раз был результат >= 16ти.

                add = result_out.popleft()      # берем последнее значение
                adding = number + add           # складываем его с текущим

                if adding >= 16:                # если получилось больше 16ти:
                    number_, count = next_count(adding)
                    result_out.appendleft(number_)
                    result_out.appendleft(count)
                else:
                    result_out.appendleft(adding)  # если меньше:

            else:                               # если результат >= 16ти и в предыдущий раз не было переноса по разрядам.
                if number >= 16:
                    number_, count = next_count(number)
                    result_out.appendleft(number_)
                    result_out.appendleft(count)
                else:
                    result_out.appendleft(number)   # если результат < 16ти и в предыдущий раз не было переноса по разрядам.
        position += 1
    return result_out

#################################################################
# основной код программы:
#################################################################

print('Программа складывает два 16ти ричных числа.')
a_number = deque(input('Введите первое число: '))
b_number = deque(input('Введите второе число: '))

a_number, b_number = align(a_number, b_number)    # выравниваем нулями меньшее число.
result = deque()

for number in range(len(a_number)):               # проходимся по числам и складываем стоящие друг под другом числа "как есть".

    summ_one = summ(a_number.pop(), b_number.pop())
    result.appendleft(summ_one)


result = normalize(result)          # нормализуем полученный результат.

print(f'Результат: {list(map(hex, result))}')       # печатаем в формате hex.







