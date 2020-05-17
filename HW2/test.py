#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов ряда чисел: '))

i = 1

#for i in range(1, n + 1):
def summa(n, summ = 1.0, number = 1.0, i = 1):

    if i == n:
        return summ

    number = number / 2

    if i % 2 == 0:
        summ = summ + number
    else:
        summ = summ - number

    return summa(n, summ, number, i+1)

print(summa(n))