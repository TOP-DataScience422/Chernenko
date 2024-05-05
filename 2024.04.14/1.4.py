a = int(input("Введите число: "))
b = "0"
c = int("1"+a*b)-1
d = c%100+1
e = []

for i in range (d, c +1):
    count = 0
    for j in range (1, i + 1):
        if i % j == 0 and i != j and j !=1:
            count += 1
    if count == 0:
        e.append(i)
print (len(e))
   
# Введите число: 3
# 143           
