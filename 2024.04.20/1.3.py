my_list_1 = [int(value) for value in input("Введите целые числа: ").split()]
my_list_2 = [int(value) for value in input("Введите целые числа: ").split()]
int_list = []
for element in my_list_2:
    int_list.append(int(element))
if my_list_1 >= int_list[::1]:
    print('Yes')
else:
    print('No')
    
# Введите целые числа: 1 2 3 4
# Введите целые числа: 1 2
# Yes

# Введите целые числа: 1 2 3 4
# Введите целые числа: 2 4
# No