a = int (input("Введите первое число: "))  
b = int (input("Введите второе число: "))  
n = float(a//b)
if n % 2 == 0:
    print (a, "делится на", b, "нацело")
    print(f'частное: {a//b}')
else:
    print (a, "не делится на", b, "нацело")
    print(f'неполное частное: {a//b}')
    print(f'остаток: {a%b}')


# Введите первое число: 8
# Введите второе число: 2
# 8 делится на 2 нацело
# частное: 4

# Введите первое число: 10
# Введите второе число: 3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1
