print('*'*45, '\nЗадание normal выполнил: Синицин Максим Анатольевич\n'+'hw_basic_less5_normal.py\n'+'*'*45)


print('\n<'+'-'*10+'>'+'1'+'<'+'-'*10+'>')

import os
import shutil
import hw_less5_easy as dirs

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def menu():
    print('''
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Удалить папку
    4. Создать папку
    5. Выход
    ''')

def input_dir_name():
    return input('Введите название папки')

if __name__ == '__main__':
    while True:
        menu()
        result = input('Выберите пункт меню: ')
        dir_name = ''
        if result == '1':
            dir_name = input_dir_name()
            dirs.change_dir(dir_name)
        elif result == '2':
            dirs.show_dirs()
        elif result == '3':
            dir_name = input_dir_name()
            dirs.rm_dir(dir_name)
        elif result == '4':
            dir_name = input_dir_name()
            dirs.mk_dir(dir_name)
        elif result == '5':
            break
        else:
            print('Неверный пункт меню')

