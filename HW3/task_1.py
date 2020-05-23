# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

big_list = [i for i in range(2, 100)]
numbers = [i for i in range(2, 10)]
answer = []

for number in numbers:
    for value in big_list:
        if value % number == 0:
           answer.append(value)

    print(f'{number} = {answer}')
    answer.clear()