def taxi_cost (cost: int, expectation: int = 0)  -> int | None:
    cost_trip = cost / 150 * 6
    cost_exp = expectation * 3
    calculation = 0
    if cost > 0 and expectation >= 0:
        calculation = int(round(80 + cost_trip + cost_exp, 0))
        return calculation
    if cost == 0 and expectation >= 0:
        calculation = int(round(80  + cost_exp + 80, 0))
        return calculation  
    else:
        return None
    
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None    
