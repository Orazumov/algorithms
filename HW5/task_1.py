# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

number = 0

company = defaultdict(list)
good_comp = []
bad_comp = []

full_benefit = 0

while not number:
    number = int(input('Введите количество предприятий больше 0: '))

for z in range(1, number + 1):
    company[f'name{z}'] = input('Введите название предприятия: ')
    for i in range(1, 5):
        company[f'benefit{z}'].append(int(input(f'Введите прибыль за {i} квартал: ')))
    company[f'annual_benefit{z}'] = sum(company[f'benefit{z}'])
    full_benefit += company[f'annual_benefit{z}']

average_benefit = full_benefit / number
print(f'Средняя прибыль компаний за год: {average_benefit}')

for z in range(1, number + 1):
    if company[f'annual_benefit{z}'] > average_benefit:
        good_comp.append(company[f"name{z}"])
    else:
        bad_comp.append(company[f"name{z}"])

print(f'Прибыльные компании: {good_comp}')
print(f'Убыточные компании: {bad_comp}')
