import math

def central_tendency(num1: float, num2: float, *numbers: float) -> dict[str, float]:
    list_dict = {}
    number = sorted ([num1, num2, *numbers])
    if len(number) % 2 !=0:
        a = int ((len(number) + 1) / 2)
        median = number[a - 1]
    else:
        b = int(len(number) / 2)
        c = int(len(number) / 2 + 1)
        median = (number[b - 1] + number[c - 1]) / 2
        
    arithmetic = sum(number) / len(number)
    geometric = math.pow(math.prod(number), 1 / len(number))
    harmonic = len(number) / sum(i ** -1 for i in number)
    list_dict  = {'median':median, 'arithmetic': arithmetic, 'geometric': geometric, 'harmonic': harmonic}
		
    return list_dict 
    
# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}