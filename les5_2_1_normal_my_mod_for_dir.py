# Библиотека для работы с папками

import os
def creat_dir():
    i = input("Введите название папки")
    dir_new = os.path.join(os.getcwd(), '{}'.format(i))
    try:
        res = os.mkdir(dir_new)
        print("Успешно создано")
    except FileExistsError:
        res = print("Невозможно создать. Такая директория уже существует")
    return(res)
def del_dir():
    i = input("Введите название папки, которую необходимо удалить")
    dir_del = os.path.join(os.getcwd(), '{}'.format(i))
    try:
        res = os.rmdir(dir_del)
        print("Успешно удалено")
    except FileNotFoundError:
        res = print("Невозможно удалить. Такой директории не существует")
    return(res)
def list_dir():
    i = os.listdir(os.getcwd())
    res = print(i)
    return(res)
def open_dir():
    i = input("Введите название папки, в которую необходимо перейти")
    dir_op = os.path.join(os.getcwd(),'{}'.format(i))
    try:
        res = os.chdir(dir_op)
        print("Успешно перейдено")
    except FileNotFoundError:
        print("Невозможно перейти. Такой директории не существует")

