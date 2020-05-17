#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# https://drive.google.com/file/d/11gScxylUltYfcgdrjz3YZsc7xxsn9b5S/view?usp=sharing

number = int(input('Введите число: '))
number_output = 0

while number:
    last_number = number % 10
    number_output += last_number
    number = number // 10
    if number:
        number_output = number_output * 10

print(f'Число в обратном порядке {number_output}')