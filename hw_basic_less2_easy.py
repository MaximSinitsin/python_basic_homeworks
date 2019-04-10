print('*'*45)
print('Задание easy выполнил: Синицин Максим Анатольевич')
print('*'*45)
print('hw_basic_less2_easy.py')
print('<'+'-'*10+'>'+'1'+'<'+'-'*10+'>')

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'банан', 'киви', 'арбуз', 'мандарин', 'грейпфрукт']
max_len = max(len(fruit) for fruit in fruits)

for number, fruit in enumerate(fruits, 1):
    print(f'{number}. {fruit:>{max_len}}')

print('<'+'-'*10+'>'+'П'+'<'+'-'*10+'>')
# ПРИМЕР ПРЕПОДАВАТЕЛЯ
fruits = ['яблоко', 'банан', 'киви', 'арбуз', 'мандарин', 'грейпфрукт', 'топинамбурик']
max_len = len(max(fruits, key=len))             # --> найдет элемент списка максим-й по длине

for number, fruit in enumerate(fruits, start=1):
    print('{}. {}'.format(number, fruit.rjust(max_len)))             # --> выравнеет по правому краю


print('<'+'-'*10+'>'+'2'+'<'+'-'*10+'>')
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

my_friends = ['Leo', 'Anton', 'Michael', 'Olga', 'Jane', 'Vera', 'Andrei']
sergei_friends = ['Leo', 'Michael', 'Jane', 'Andrei']

for friend in my_friends:
    if friend in sergei_friends:
        my_friends.remove(friend)
print(my_friends)

# второй вариант в одну строчку
print(list(i for i in my_friends if i not in sergei_friends))

print('<'+'-'*10+'>'+'П'+'<'+'-'*10+'>')
# ПРИМЕР ПРЕПОДАВАТЕЛЯ
my_friends = ['Leo', 'Anton', 'Michael', 'Olga', 'Jane', 'Vera', 'Andrei']
sergei_friends = ['Leo', 'Michael', 'Jane', 'Andrei']

for friend in sergei_friends:
    while friend in my_friends:
        my_friends.remove(friend)
print(my_friends)


print('<'+'-'*10+'>'+'3'+'<'+'-'*10+'>')
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

listing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12]
new_listing = []

for i in listing:
    if i % 2 == 0:
        new_listing.append(i/4)
    else:
        new_listing.append(i*2)
print(new_listing)


print('<'+'-'*10+'>'+'П'+'<'+'-'*10+'>')
# ПРИМЕР ПРЕПОДАВАТЕЛЯ
# нет замечаний - все ок



print('*'*45)

