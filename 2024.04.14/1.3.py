n = int(input("Введите число: "))
sum = 0
for i in range(1,n+1):
    if n % i == 0 :
        sum += i
print(sum)

# Введите число: 50
# 93