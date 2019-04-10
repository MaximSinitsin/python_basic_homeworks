print('РЕШЕНИЯ ПРЕПОДАВАТЕЛЕЙ')

# Задание-1: уравнение прямой вида y = kx + b задано ввиде строки.
# Определить координату y, точки с заданной координатой x
# вычислите и выведите y

print('*'*45)
print('Задание hard')
print('*'*45)
print('hw_basic_less2_hard.py')
print('')
print('<'+'-'*10+'>'+'1'+'<'+'-'*10+'>')

# вариант № 1
equation = ' y = -12x + 11111140.2121'
x = 2.5
k_i = 0
k_j = 0
b_i = 0

for i in range(len(equation)):
    if equation[i] == '=':
        k_i = i
    elif equation[i] == 'x':
        k_j = i
    elif (equation[i] == '+' or equation[i] == '-') and k_j > 0:
        operation = int(equation[i]+'1')
        b_i = i

k = float(equation[k_i+1:k_j])
b = float(equation[b_i+1:])

y = k * x + operation * b
print(y)


# вариант № 2 ЛУЧШЕ
equation = ' y = -12x + 11111140.2121'
x = 2.5

split_result = equation.split()         # --> ['y', '=', '-12x', '-', '11111140.2121'] разбиваем строку по пробелу
number_with_x = float(split_result[2].replace('x', '')) * x         # -->-30.0

# так как условием четко прописано сложение, то другие варианты здесь не учитываем
# добавляется несколько условий
y = number_with_x + float(split_result[4])
print(y)

print('')
print('<'+'-'*10+'>'+'2'+'<'+'-'*10+'>')

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена дата
# Условия коррекности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)


# вариант № 1 СЛОЖНО
date = input('Введите дату в формате dd.mm.yyyy: ')
flag_date = False

while flag_date == False:
    j = 0
    flag_lenght = False
    flag_point = False
    flag_range = False

# поиск точек в дате и проерка на корректность точек в записи
    for i in range(len(date)):
        if date[i] == '.' and j == 0:
            j += 1
            day_point = i
        elif date[i] == '.' and j == 1:
            month_point=i
            j += 1
            flag_point = True

# флаг точек истина можно проверять длинну кол-ва символов для даты месяца и года
    if flag_point:
        if len(date[:day_point]) == 2 and len(date[day_point+1:month_point])== 2 and len(date[month_point+1:]) == 4:
            flag_lenght = True

# Если флаг длины символов истина, то можно проверять коректность диапазона
        if flag_lenght:
            day = date[:day_point]
            month = date[day_point + 1:month_point]
            year = date[month_point + 1:]
            if (int(day) >= 1 and int(day) <= 31) and (int(month) >= 0 and int(month) <= 12) and (int(year) >= 1 and int(year) <= 9999):
                flag_range = True

    if flag_point and flag_lenght and flag_range:
        flag_date = True
        print('Дата корректная')
    else:
        print('Дата введена не корректно')
        date = input('Введите корректную дату в формате dd.mm.yyyy:')

# вариант № 2  ЛУЧШЕ
days_count_by_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
date = input('Введите дату: ')
day, month, year = date.split('.')

if len(day) == 2 and len(month) == 2 and len(year) == 4:
    if 0 < int(month) <= 12 \
            and 0 < int(year) <= 9999 \
            and 0 < int(day) <= days_count_by_month[int(month)]:
        print('Дата коректна.')
    else:
        print('Дата не коректна.')
else:
    print('Длины одной из частей даты не коректна.')



print('')
print('<'+'-'*10+'>'+'3'+'<'+'-'*10+'>')

# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научится по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

# ВАРИАНТ 1 - пипец сложно
flag_quit = False
while flag_quit != True:
    floor_count_room = []
    first_room_in_floor = []
    number_romm = input('Введите номер комнаты: ')
    number_floor = 1
    count_first_room = 1
    count_room = 0
    count_floor = 0
    count_position = 0
    flag_room = False
    i = 0
    while flag_room != True:
        i += 1
        print('квадрат этаже - ', i)
        for j in range(0, i):
            floor_count_room.append(i)
            first_room_in_floor.append(count_first_room)
            count_floor += 1
            #print('Захожу на этаж', count_floor)
            count_position = 0
            for z in range(count_first_room, count_first_room + i):
                count_position += 1
                count_room += 1
                print(count_room)
                if int(number_romm) == count_room:
                    print('номер этажа:', count_floor)
                    print('номер слева:', count_position, )
                    flag_room = True
            count_first_room += i

    quit = input('Выход? yes/no: ')
    if quit == 'yes':
        flag_quit=True

# ВАРИАНТ 2 - ЛУЧШЕ - очень просто

room_for_search = int(input('Номер искомой комнаты: '))

block = 1
first_room = 1
stage = 1

while room_for_search >= first_room + block ** 2:
    first_room = first_room + block ** 2
    stage += block
    block += 1

stage += ((room_for_search - first_room) // block)
room_sequence = int((room_for_search - first_room) % block + 1)

print(stage, room_sequence)


print('')
print('*'*45)
print('')

