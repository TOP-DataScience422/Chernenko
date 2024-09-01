from numpy import array, average
import numpy as np

print(f'вариант 7\nПроверка гипотезы о нормальном распределении по ряду N\n')
N = array([101, 136, 123, 142, 111, 155, 136, 168, 131, 185])
n = 10
u_a = 0.461
N_mean = average(N)
N_var = np.var(N)
N_std = N_var ** 0.5

ListN= []
a =  [(i-N_mean) / N_std for i in N]
ListN.append(a)

ListN_1 = [0.5821, 0.452, 0.2578, 5517, 0.1251, 7486, 0.4562, 0.8869, 0.3783, 0.7257]

for index, item in enumerate(ListN_1, 1):
        u = (1 / 12 * n) + (item - (2*index-1)/(2*9))**2
if u < u_a:
    print(f'{u:.3F} <  {u_a}\nосновная гипотеза принята')
else:
    print(f'{u:.3F} >  {u_a}\nосновная гипотеза отвергнута')
 
print(f'\nПроверка гипотезы о нормальном распределении по ряду R\n')
R = array([162, 181, 173, 182, 171, 186, 185, 199, 171, 192, 181, 210, 187, 213])
n1 = 14

R_mean = average(R)
R_var = np.var(R)
R_std = R_var ** 0.5

ListR= []
a =  [(i-R_mean) / R_std for i in N]
ListR.append(a)

ListR_1 = [0.1, 0.2326, 0.5168, 0.1107, 0.6821, 0.1618, 0.2326, 0.1075, 0.6152, 0.496]

for index, item in enumerate(ListR_1, 1):
        u_R = (1 / 12 * n1) + (item - (2*index-1)/(2*9))**2
if u_R < u_a:
    print(f'{u_R:.3F} <  {u_a}\nосновная гипотеза принята')
else:
    print(f'{u_R:.3F} >  {u_a}\nосновная гипотеза отвергнута')
