#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

# https://drive.google.com/file/d/11gScxylUltYfcgdrjz3YZsc7xxsn9b5S/view?usp=sharing

for i in range(32, 128):
    if i % 10 == 1 and i > 32:
        print(f'{i}-{chr(i)}|', end='\n')
    else:
        print(f'{i}-{chr(i)}|', end='')
