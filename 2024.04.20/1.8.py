l = str(input('Введите значение: '))
result = list()
my_list = l.split('; ')
for fname in my_list:
    orig = fname
    i=1
    while fname in result :
        fname = '.'.join(orig.split('.')[:1]) + "_"+str(i)+'.'+'.'.join(orig.split('.')[1:])
        i += 1
    result.append(fname)
from pprint import pprint
pprint(sorted(result))

# Введите значение: 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# ['1.py',
 # '1_1.py',
 # '1_2.py',
 # 'aux.h',
 # 'functions.h',
 # 'main.cpp',
 # 'main_1.cpp',
 # 'main_2.cpp',
 # 'src.tar.gz',
 # 'src_1.tar.gz']