def countable_nouns (number:int, tuple1:[str, str, str]) -> str:
    if number % 10 == 1 and number != 11:
        return tuple1[0]
    elif number % 10 == 2 and number != 12 or number % 10 == 3 and number != 13 or number % 10 == 4 and number != 14:
        return tuple1[1]
    else:
        return tuple1[2]
        
 # >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'