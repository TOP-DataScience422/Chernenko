email = input("Введите адрес электронной почты: ")
counter = email.count("@")
toch = email.split('@')
counter1 = toch[1].count('.')
if counter == 1 and counter1 == 1:
    print('Yes')
else:
    print('No')

# Введите адрес электронной почты: sgd@ya.ru
# Yes

# Введите адрес электронной почты: abcde@fghij
# No
   