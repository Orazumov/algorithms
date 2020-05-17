#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# https://drive.google.com/file/d/11gScxylUltYfcgdrjz3YZsc7xxsn9b5S/view?usp=sharing

print('Программа четные и нечетные числа пользовательского числа.')

num = int(input('Введите число: '))

def count_numbers(num, even_num=0, odd_num=0):
    if num == 0:
        return f'Четных цифр {even_num}, Нечетных цифр {odd_num}'
    if num % 10 % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    return count_numbers(num // 10, even_num, odd_num)

print(count_numbers(num, odd, even))

# Вариант с циклом:

#for i in number:
#    if int(i) % 2 == 0:
#        even += 1
#    else:
#        odd += 1

#print(f'Четных цифр: {even}')
#print(f'Нечетных цифр: {odd}')
