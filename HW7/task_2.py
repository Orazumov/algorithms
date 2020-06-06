from random import uniform

SIZE = 10
array = [round(uniform(0, 49), 2) for _ in range(SIZE)]
print(f'Массив до сортировки слиянием: {array}')

# слияние отсортированных массивов.

def merge(A:list, B:list):
    C = [0]*(len(A) + len(B)) # зарезервировали нужное количество памяти под фин. массив.
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:   # если < будет неустойчиво!
            C[n] = A[i]; i += 1; n += 1 # мы берем из А, чтобы сорт была устойчивой, т.е. чтобы не менять порядок равных элементов.
        else:
            C[n] = B[k]; k += 1; n += 1
    while i < len(A):   # заливаем оставшиеся элементы, если B закончился.
        C[n] = A[i]; i += 1; n += 1
    while k < len(B):  # заливаем оставшиеся элементы, если А закончился.
        C[n] = B[k]; k += 1; n += 1
    return C

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):   # перелили в А. Можно сделать срезами.
        A[i] = C[i]   # просто А=С нельзя, т.к. просто поменяем ссылку.

    return A

print(f'Массив после сортировки слиянием: {merge_sort(array)}')

