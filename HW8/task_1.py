#Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
# вернуть количество различных подстрок в этой строке.
#Примечание: в сумму не включаем пустую строку и строку целиком.
#Пример работы функции:

#func("papa")
#6
#func("sova")
#9

string = input('Введите строку из латинских буква: ')

def hash(string:str):
    array = []

    for index1 in range(len(string)):
        for index2 in range(index1, len(string)):
            if not (index1 == 0 and index2 == len(string)-1):
                array.append(string[index1:index2+1])
    array = set(array)

    return len(array)

print(hash(string))
