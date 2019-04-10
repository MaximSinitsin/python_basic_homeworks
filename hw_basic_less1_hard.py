print('*'*45)
author = 'Синицин Максим Анатольевич'
print('Задание выполнил:', author)
print('*'*45)
print('hw_basic_less1_hard.py')
print('<'+'-'*10+'>'+'1'+'<'+'-'*10+'>')

# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в
# -     хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг, (< 30 лет и вес >50 и <120)
# Пациенту
# -     требуется начать вести правильный образ жизни, если ему (> 30 и < 40; и вес < 50 или > 120 кг)
# Пациенту
# -     требуется врачебный осмотр, если ему (> 40 и вес < 50 или > 120 кг.)
#
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

print('Медицинская анкета работоспособности.')
print('-'*19)
your_year = int(input('Введите Ваш год рождения: '))
age = 2019 - your_year
print('Тебе {} '.format(age))
access = 0
if age < 18 or age > 65:
    print('Извините, пользование данным ресурсом возможно только с 18 до 65 лет!')
    print('До свидания!')
    access = 0
else:
    print('Доступ к ресурсу разрешен')
    access = 1
while access == 0:
    pass

name = input('Ваше имя: ')
surname = input('Ваше фамилия: ')
weight = int(input('Ваш вес: '))
print('-'*19)

good = ' - Ваше сосотояние здоровья - ОТЛИЧНОЕ! Продолжайте в том же духе!'
middle = ' - Задумайтесь, Вам надо заняться собой и своим здоровьем! Телефон ближайшего спортклуба 999-99-99'
bad = ' - Вам следует обратиться к врачу! Телефон поликлиники 333-33-33'

if age >= 18 and age <= 30 and weight >= 50 and weight <= 90 or age > 30 and age <= 65 and weight >= 60 and weight <= 120:
    result_good = 'Ваш результат: {name} {surname}, возраст:{age}, вес:{weight},{good}'.format(name=name, surname=surname, age=age, weight=weight, good=good)
    print(result_good)

elif age >= 18 and age <= 30 and weight >= 30 and weight <= 50 or weight >= 90 and weight <= 120\
                                or age > 30 and age <= 65 and weight >= 30 and weight <= 60 or weight >= 120 and weight <= 130:

    result_middle = 'Ваш результат: {name} {surname}, возраст:{age}, вес:{weight},{middle}'.format(name=name, surname=surname, age=age, weight=weight, middle=middle)
    print(result_middle)

elif age >= 18 and age <= 65 and weight < 30 or weight > 130:
    result_bad = 'Ваш результат: {name} {surname}, возраст:{age}, вес:{weight}, {bad}'.format(name=name, surname=surname, age=age, weight=weight, bad=bad)
    print(result_bad)

print('-'*19)
print('Жедаем успехов и здоровья!')
