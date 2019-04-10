print('*'*45, '\nЗадание easy выполнил: Синицин Максим Анатольевич\n'+'hw_basic_less5_easy.py\n'+'*'*45)


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

def mkdirs():
    [os.mkdir('dir_' + str(i)) for i in range(1, 10) if not os.path.exists('dir_' + str(i))]
def rmdirs():
    [os.rmdir('dir_' + str(i)) for i in range(1, 10) if os.path.exists('dir_' + str(i))]

# чтобы увидеть созданные файлы - надо: внизу ЗАкомметировать rmdirs()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dirs():
    print([i for i in os.listdir() if os.path.isdir(i)])


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    shutil.copyfile(__file__, __file__ + '.copy')
# чтобы создать копию файла - надо: внизу РАСкомметировать copy_file()


if __name__ == '__main__':
    mkdirs()
    rmdirs()      # --> ЗАкомментировать чтобы отработалось создание файлов dir_1-dir_10
    list_dirs()
    # copy_file()      # --> РАСкомметировать copy_file() - чтобы создать копию файла



# для задания нормал:
def change_dir(new_dir):
    if os.path.exists(new_dir):
        os.chdir(new_dir)
    else:
        print('Такой папки не существует')


def show_dirs():
    print(os.listdir())


def rm_dir(del_dir):
    if os.path.exists(del_dir):
        os.rmdir(del_dir)
    else:
        print('Папки не существует')


def mk_dir(new_dir):
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    else:
        print('Папка с таким именем существует')

