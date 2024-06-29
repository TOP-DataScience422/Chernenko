my_number = input("Введите число: ")
my_set = set()
b = {0, 1}
if my_number.startswith('b') or my_number.startswith('0b') or my_number.startswith('0') or my_number.startswith('1') and not my_number.startswith('1b') and not my_number.startswith('0b'):
    my_set = set(int(i) for i in my_number[2:])
    if my_set <= b:
        print('да')
else:
    print('нет')
    
# Введите число: 0101
# да
# Введите число: b11
# да
# Введите число: 0b11001
# да
# Введите число: 1b0101
# нет
