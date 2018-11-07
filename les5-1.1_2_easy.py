# Задача-1 (part2 - Удаление папок):
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
i = 0
while i<9:
    i+=1
    dir_del = os.path.join(os.getcwd(), 'dir_{}'.format(i))
    try:
        os.rmdir(dir_del)
    except FileNotFoundError:
        print("Такой директории не существует")
