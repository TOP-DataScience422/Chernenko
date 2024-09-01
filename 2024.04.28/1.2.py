spis = ['черви', 'бубны', 'пики', 'трефы']
def deck()-> tuple[int, str]:
    for i in spis:
        for j in range(2, 15):
            yield j,i
            
            
# >>> print(*list(deck())[::13])
# (2, 'черви') (2, 'бубны') (2, 'пики') (2, 'трефы')