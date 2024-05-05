n = int(input('Введите число: '))
a1 = a2 = 1
print (a1, end = ' ')
for i in range(2, n):
 a1, a2 = a2, a1 + a2
 print(a2, end=' ')
 
 # Введите число: 17
# 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597