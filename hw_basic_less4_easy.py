print('*'*45, '\nЗадание easy выполнил: Синицин Максим Анатольевич\n'+'hw_basic_less4_easy.py\n'+'*'*45)

# Все задачи текущего блока решите с помощью генераторов списков!

print('\n<'+'-'*10+'>'+'1'+'<'+'-'*10+'>')
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# 1 вариант:
import random
r = [random.randint(1, 10) for _ in range(10)]
print(list(i ** 2 for i in r))


# 2 вариант:
a = [1, 2, 4, 0]
b = []
print(list(map(lambda x: x ** 2, a)))


print('\n<'+'-'*10+'>'+'2'+'<'+'-'*10+'>')
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits_1 = ['банан', 'яблоко', 'мандарин', 'ананас']
fruits_2 = ['грейпфрукт', 'яблоко', 'манго', 'ананас']
print('Список фруктов номер 1: ', fruits_1)
print('Список фруктов номер 2: ', fruits_2)

# 1 вариант:
print(list(i for i in fruits_1 if i in fruits_2))


# 2 вариант:
print(list(filter(lambda x: x in fruits_2, fruits_1)))


print('\n<'+'-'*10+'>'+'3'+'<'+'-'*10+'>')
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
numbers = [random.randint(-100, 100) for i in range(10)]
print('Список случайных чисел: ', numbers)
print('Положительные числа кратные 3 и некратные 4: ', list(number for number in numbers if number % 3 == 0\
                                                            and number > 0 and number % 4 != 0))


print('\n'+'*'*45)