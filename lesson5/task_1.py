# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Company = namedtuple('Company', ['name', 'quarters', 'income'])
result_list = []
sum_income = 0
how_much_companys = int(input("Введите количество компаний: "))

i = 1
while i <= how_much_companys:
    quarter = []
    name = input("Введите название компании: ")

    for itm in range(4):
        quarter.append(int(input(f"Введите прибыл '{name}' за {itm + 1} квартал: ")))

    income = sum(quarter)
    company = Company(name=name, quarters=quarter, income=income)
    result_list.append(company)
    sum_income = sum_income + income

    i += 1

avg_all_income = sum_income / how_much_companys
print(f'Средняя прибыль всех компаний за год - {avg_all_income}.')

max_comps = []
min_comps = []
avg_comps = []
for company in result_list:
    if company.income > avg_all_income:
        max_comps.append(company.name)
    elif company.income < avg_all_income:
        min_comps.append(company.name)
    else:
        avg_comps.append(company.name)

print(f'Компании с прибылью выше среднего - {max_comps}.\n'
      f'Компании со средней прибылью - {avg_comps}.\n'
      f'Компании с прибылью ниже среднего - {min_comps}.')