# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys

a = sys.argv
b = str(a[0])
m = b.split("\\")
n = m[-1:]
k = str(n[0])
c = k[:-3]
d = '{}_copy.py'.format(c)
old_file = open(k, 'r', encoding = 'utf-8').read()
new_file = open(d, 'w', encoding = 'utf-8')
new_file.write(old_file)
new_file.close()
