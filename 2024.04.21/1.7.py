_dict = "0123456789abcdefghijklmnopqrstuvwxyz"
numbers = range(0, 36)
my_dict = dict(zip(_dict, numbers))
def base(number: str, base: int) -> str:
    result = ''
    num = int(number)
    while num != 0:
        a = num % base
        for i,j in my_dict.items():
            if a == j:
                result += i
        num = num // base
    return result[::-1]
    
def arg (number: str, base: int) -> str:
    return str(int(number, base))
    
def int_base(number: str, base1: int, base2: int) ->str:
    return base(arg(number, base1), base2)
    
# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3g'
# >>>