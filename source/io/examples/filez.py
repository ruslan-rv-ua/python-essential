Файл , основні операції
потоки
курсор файла
стандартні потоки, термінал
import sys
print(sys.stdin)
print(sys.stdout)
print(sys.stderr)
буферізація - блочна і порядкова
from time import sleep

print('hello ', end='', flush=True)
sleep(5)
print('world')

дескриптор файла

import os
print(os.open)

open - в модулі io
import io
io.open is open

from os.path import join
join('..','windows','system32')

чому різні режими відкриття файлів, перегони

