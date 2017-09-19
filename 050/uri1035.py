#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())

leitura = input().split(' ')

a, b, c, d = leitura


if int(b) > int(c) and int(d) > int(a) and (int(c)+int(d)) > (int(a)+int(b)) \
        and int(c) >= 0 and int(d) >= 0 and int(a) >= 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')