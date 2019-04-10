print('*'*45)
print('Задание normal выполнил: Синицин Максим Анатольевич')
print('*'*45)
print('hw_basic_less3_normal.py')
print('\n<'+'-'*10+'>'+'1'+'<'+'-'*10+'>')

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

def vax(x):
    return x * 87 // 100

workers = ['Ivanov', 'Petrov', 'Sidorov', 'Vasechkin', 'Maksimov', 'Viktorov']
salaries = [20000, 35000, 690000, 340000, 120000, 700000]

list_salary = dict(zip(workers, salaries))
print('Общая ведомость начисления заработной платы:\n'+'-'*45)
print(list_salary, '\n')


salaries_vax = list(map(vax, salaries))
list_salary = dict(zip(workers, salaries_vax))
print('Общая ведомость заработной платы с учетом налога 13%:\n'+'-'*53)
print(list_salary, '\n')


with open('salary.txt', 'w', encoding='utf-8') as file:
    for worker, salary in list_salary.items():
        if salary <= 500000:
            file.write('{} - {}\n'.format(worker.upper(), salary))

file = open('salary.txt', 'r', encoding='utf-8')
file.seek(0)
print('Итоговая ведомость заработной платы:\n'+'-'*40)
print(file.readlines())
file.close()


'''
print('-'*53)
# вариант преподавателя
names = ['Ivanov', 'Petrov', 'Sidorov', 'Vasechkin', 'Maksimov', 'Viktorov']
salary = [20000, 35000, 690000, 340000, 120000, 700000]

TAX_PERCENT = 13
MAX_SALARY = 500000

result = dict(zip(names, salary))

f = open('salary2.txt', 'w+', encoding='UTF-8')

for key, value in result.items():
    if value <= MAX_SALARY:
        f.write('{} - {}\n'.format(key.upper(), value))
f.seek(0)

for line in f:
    name, salary = line.split(' - ')
    tax = int(salary) / 100 * TAX_PERCENT
    after_tax = int(salary) - int(tax)
    print('{} получил зарплату в размере: {}, налог составил: {}'.format(name.upper(), after_tax, tax))
f.close()
'''
print('*'*45)

