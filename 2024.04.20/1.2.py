a = input('Введите название фруктов: ')
fruits = [a]
while a != '':
    a = input('Введите название фруктов: ')
    fruits.append(a)
fruits.pop()
b = fruits.pop()
print(*fruits, sep=', ', end = ' и ')
print(b)

# Введите название фруктов: яблоко
# Введите название фруктов: груша
# Введите название фруктов:
# яблоко и груша

# Введите название фруктов: яблоко
# Введите название фруктов: груша
# Введите название фруктов: апельсин
# Введите название фруктов:
# яблоко, груша и апельсин

# Введите название фруктов: яблоко
# Введите название фруктов: груша
# Введите название фруктов: апельсин
# Введите название фруктов: лимон
# Введите название фруктов:
# яблоко, груша, апельсин и лимон

