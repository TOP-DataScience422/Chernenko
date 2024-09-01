def math_function_resolver(func: 'function', *x: float, res: bool = False) -> list:
    result = list(map(func, x))
    result = list(map(lambda x: str(round(x)), result))
    return result
    
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# ['2', '3', '4', '4', '4', '5', '6', '6', '6']
# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# ['2', '1', '0', '0', '0', '-1', '-2', '-2', '-2']
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), res=True)
# ['3', '7', '20', '55', '149', '405', '1101', '2996', '8149']