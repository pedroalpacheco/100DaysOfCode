import numpy as np

numero = float(input())

#intervalo 0-25
zero25 = np.linspace(0.00,25.00)

#intervalo 25-50
zero50 = np.linspace(25.00,50.00)

#intervalo 50-75
zero75 = np.linspace(50.00,75.00)

#intervalo 75-100
zero50 = np.linspace(75.00,100.00)


respzero25 = numero in zero25
respzero50 = numero in zero25
respzero75 = numero in zero25
respzero100 = numero in zero25

if respzero25 == True:
    print('Intervalo [0,25]')
elif respzero50 == True:
    print('Intervalo (25,50]')
elif respzero75 == True:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')

