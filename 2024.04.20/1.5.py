my_list_1 = input("Введите слово: ")
scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
a = []
total = int()
for i in my_list_1:
    a.append(i)
for k, v in scores_letters.items():
    for j in a:
        if j in v.lower():
            total += k
print (total)

# Введите слово: синхрофазотрон
# 29