import math

numeros = input().split(' ')

a, b, c = numeros

x = (float(b)**2)-(4*float(a)*float(c))

if x < 0:
    print('Impossivel calcular')


else:
    try:
        x = math.sqrt(x)
        r1 = (-float(b) + float(x)) / (2 * float(a))
        r2 = (-float(b) - float(x)) / (2 * float(a))
        print('R1 = {:.5f}'.format(r1))
        print('R2 = {:.5f}'.format(r2))
    except ZeroDivisionError:
        print("Impossivel calcular");

