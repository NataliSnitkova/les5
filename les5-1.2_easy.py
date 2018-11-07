# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
a = os.listdir(os.getcwd())
print(a)