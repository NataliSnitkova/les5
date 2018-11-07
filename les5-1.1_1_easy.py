# Задача-1 (part1 - создание папок):
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
i = 0
while i<9:
    i+=1
    dir_new = os.path.join(os.getcwd(), 'dir_{}'.format(i))
    try:
        os.mkdir(dir_new)
    except FileExistsError:
        print("Такая директория уже существует")
